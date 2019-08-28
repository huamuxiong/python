#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from flask import current_app, g, request, jsonify
from alipay import AliPay

from . import api
from ihome.utils.commons import login_required
from ihome.models import Order
from ihome.utils.response_code import RET
from ihome import constants, db


# POST 127.0.0.1:5000/api/v1.0/orders/<orderId>/payment

@api.route("/orders/<int:order_id>/payment", methods=['POST'])
@login_required
def order_pay(order_id):
    """发起支付宝支付"""

    # 获取用户的id
    user_id = g.user_id

    # 判断订单状态
    try:
        order = Order.query.filter(Order.id==order_id, Order.user_id==user_id, Order.status=="WAIT_PAYMENT").first()
    except Exception as e:
        current_app.logger.errer(e)
        return jsonify(errno=RET.DBERR, errmsg='数据库异常')

    if order is None:
        return jsonify(errno=RET.NODATA, errmsg='订单数据有误')


    # 创建支付宝sdk的工具对象
    alipay_client = AliPay(
        appid="2016101000651363",
        app_notify_url=None,
        app_private_key_path=os.path.join(os.path.dirname(__file__), "keys/app_private_key.pem"),
        alipay_public_key_path=os.path.join(os.path.dirname(__file__), "keys/alipay_public_key.pem"),
        sign_type="RSA2",
        debug=True
    )

    # 手机网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string
    order_string = alipay_client.api_alipay_trade_wap_pay(
        out_trade_no=order.id,
        total_amount=str(order.amount/100.0),
        subject='爱家租房 %s' % order.id,
        return_url="http://127.0.0.1:5000/payComplete.html",
        notify_url=None  # 可选, 不填则使用默认notify url
    )

    # 构建让用户跳转的支付链接地址
    pay_url = constants.ALIPAY_URL_PREFIX + order_string
    return jsonify(errno=RET.OK, errmsg="OK", data={"pay_url": pay_url})


# put 127.0.0.1:5000/api/v1.0/order/payment

@api.route("/order/payment", methods=['PUT'])
@login_required
def save_order_payment_result():
    """保存支付订单结果
    支付成功后跳转到payComplete.html页面,
    url如：http://127.0.0.1:5000/payComplete.html
        ?charset=utf-8
        &out_trade_no=3
        &method=alipay.trade.wap.pay.return
        &total_amount=4500.00
        &sign=Givnobw%2FNN832970v....FNN8329
        &trade_no=2019082622001498191000030983
        &auth_app_id=2016101000651363
        &version=1.0
        &app_id=2016101000651363
        &sign_type=RSA2
        &seller_id=2088102178900710
        &timestamp=2019-08-26+17%3A41%3A35
    当在payComplete.html点击“返回订单”时, 向后端发起请求,将数据保存,订单的状态改为“待评价”
    """

    alipay_dict = request.form.to_dict()

    # # 对支付宝的数据进行分离  提取出支付宝的签名参数sign 和剩下的其他数据
    alipay_sign = alipay_dict.pop("sign")

    # 创建支付宝sdk的工具对象
    alipay_client = AliPay(
        appid="2016101000651363",
        app_notify_url=None,
        app_private_key_path=os.path.join(os.path.dirname(__file__), "keys/app_private_key.pem"),
        alipay_public_key_path=os.path.join(os.path.dirname(__file__), "keys/alipay_public_key.pem"),
        sign_type="RSA2",
        debug=True
    )

    # 借助工具验证参数的合法性
    # 如果确定参数是支付宝的，返回True，否则返回false
    result = alipay_client.verify(alipay_dict, alipay_sign)

    if result:
        # 修改数据库的订单状态信息
        order_id = alipay_dict.get("out_trade_no")
        trade_no = alipay_dict.get("trade_no")  # 支付宝交易的流水号
        try:
            Order.query.filter_by(id=order_id).update({"status": "WAIT_COMMENT", "trade_no": trade_no})
            db.session.commit()
        except Exception as e:
            current_app.logger.error(e)
            db.session.rollback()

    return jsonify(error=RET.OK, errmsg='OK')


