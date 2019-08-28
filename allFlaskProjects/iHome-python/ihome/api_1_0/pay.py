#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from flask import current_app, g, request, jsonify
from alipay import Alipay

from . import api
from ihome.utils.commons import login_required
from ihome.models import Order
from ihome.utils.response_code import RET
from ihome import constants


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
    alipay_client = Alipay(
        appid="2016101000651363",
        app_notify_url=None,
        app_private_key_path=os.path.join(os.path.dirname(__file__), "keys/private_key.pem"),
        alipay_public_key_path=os.path.join(os.path.dirname(__file__), "keys/zfb_public_key.pem"),
        sign_type="RSA2",
        debug=True
    )

    # 手机网站支付，需要跳转到https://openhome.alipaydev.com/gateway.do+order_string

    order_string = alipay_client.api_alipay_trade_way_pay(
        out_trade_no=order.id,
        total_amount=str(order.amount/100.0),
        subject="爱家租房 %s" % order.id,
        return_url="127.0.0.1:5000/orders.html",
        notify_url=None
    )

    # 构建让用户跳转的支付链接地址
    pay_url = constants.ALIPAY_URL_PREFIX + order_string
    return jsonify(errno=RET.OK, errmsg="OK", data={"pay_url": pay_url})
