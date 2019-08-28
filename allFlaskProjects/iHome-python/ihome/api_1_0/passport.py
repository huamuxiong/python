#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from flask import request, jsonify, current_app, session
from sqlalchemy.exc import IntegrityError

from . import api
from ihome.utils.response_code import RET
from ihome import redis_store, db, constants
from ihome.models import User


@api.route("/users", methods=["POST"])
def register():
    """注册
    请求的参数：手机号，短信验证码，密码
    参数格式：json
    """
    # 获取参数：获取请求的json数据，返回字典
    req_dict = request.get_json()

    mobile = req_dict.get('mobile')
    sms_code = req_dict.get('sms_code')
    password = req_dict.get('password')
    password2 = req_dict.get('password2')

    # 检验参数的完整性
    if not all([mobile, sms_code, password]):
        return jsonify(errno=RET.PARAMERR, errmsg='请求参数不完整')

    # 判断手机号格式
    if not re.match(r"1[34578]\d{9}", mobile):
        return jsonify(errno=RET.PARAMERR, errmsg='手机号格式不正确')

    # 判断两次密码是否一致
    if password != password2:
        return jsonify(errno=RET.PARAMERR, errmsg='两次密码不一致')

    # 验证短信验证码是否正确
    # 从redis中取出手机号对应的短信验证码
    try:
        real_sms_code = redis_store.get("sms_code_%s" % mobile)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='读取短信验证码异常')

    # 判断是否过期
    if real_sms_code is None:
        return jsonify(errno=RET.NODATA, errmsg='短信验证码失效')

    # 将用户输入的短信验证码与redis中的短信验证码进行比较
    if sms_code != real_sms_code.decode('utf-8'):
        return jsonify(errno=RET.DATAERR, errmsg='短信验证码填写错误')

    # 判断手机号是否注册过，将注册信息保存到数据库中
    user = User(name=mobile, mobile=mobile)

    user.password = password
    # from sqlalchemy.exc import IntegrityError
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError as e:
        # 数据库操作错误后回滚
        db.session.rollback()
        # 表示手机号出现了重复，即手机号被注册过了
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAEXIST, errmsg='手机号已注册')
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='数据库查询异常')

    # 将登陆状态保存到session中
    session['name'] = mobile
    session['mobile'] = mobile
    session['user_id'] = user.id

    # 返回结果
    return jsonify(errno=RET.OK, errmsg='注册成功')


# POST 127.0.0.1:5000/sessions

@api.route('/sessions', methods=['POST'])
def login():
    """登陆
    传递参数： 手机号、密码，
    格式为：json
    """
    # 获取参数
    req_dict = request.get_json()
    mobile = req_dict.get('mobile')
    password = req_dict.get('password')

    # 验证参数的完整性
    if not all([mobile, password]):
        return jsonify(errno=RET.PARAMERR, errmsg='参数不完整')

    # 验证手机号的格式
    if not re.match(r'1[34578]\d{9}', mobile):
        return jsonify(errno=RET.PARAMERR, errmsg='手机号格式错误')

    # 判断登陆错误的次数，超过限制，则返回
    user_ip = request.remote_addr  # 获取用户的ip地址
    try:
        access_nums = redis_store.get('access_num_%s' % user_ip)
    except Exception as e:
        current_app.logger.error(e)
    else:
        if access_nums is not None and int(access_nums) > constants.LOGIN_ERROR_MAX_TIMES:
            return jsonify(errno=RET.REQERR, errmsg='登陆失败次数过多，请稍后重试')

    # 从数据库中查询用户手机号对应的对象数据
    try:
        user = User.query.filter_by(mobile=mobile).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='获取用户信息失败')

    # 将用户填写的密码与数据库中的密码进行对比验证
    if user is None or not user.check_password(password):
        try:
            # 如果验证失败，记录错误次数，返回信息
            redis_store.incr('access_num_%s' % user_ip)
            redis_store.expire('access_num_%s' % user_ip, constants.LOGIN_ERROR_FORBID_TIME)
        except Exception as e:
            current_app.logger.error(e)
        return jsonify(erno=RET.DATAERR, errmsg='手机号或密码错误')

    # 如果验证成功，保存登陆状态至session中
    session['name'] = user.name
    session['mobile'] = user.mobile
    session['user_id'] = user.id

    return jsonify(errno=RET.OK, errmsg='登陆成功')


@api.route('/session', methods=['GET'])
def check_login():
    """检查登陆状态"""
    # 尝试从session中获取用户的名字
    name = session.get('name')
    # 如果session中的name存在，则表示已经登陆，否则未登录
    if name is not None:
        return jsonify(errno=RET.OK, errmsg='true', data={"name": name})
    else:
        return jsonify(errno=RET.SESSIONERR, errmsg='false')


@api.route('/session', methods=['DELETE'])
def logout():
    """退出"""
    # 清除session数据
    session.clear()
    return jsonify(errno=RET.OK, errmsg='ok')
