#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 用户资料

from flask import g, request, current_app, jsonify, session

from . import api
from ihome.utils.commons import login_required
from ihome.utils.response_code import RET
from ihome.utils.image_storage import storage
from ihome.models import User
from ihome import db, constants


@api.route('/users/avatar', methods=['POST'])
@login_required
def set_user_avatar():
    """
    设置用户的头像
    参数：图片(对媒体表单格式)， 用户id->g.user_id
    """
    # 装饰器中的代码已经将user_id保存到g中，所以视图中可以直接读取
    user_id = g.user_id

    # 获取图片
    image_file = request.files.get('avatar')

    # 判断是否上传图片
    if image_file is None:
        return jsonify(errno=RET.PARAMERR, errmsg='图片未上传')

    image_data = image_file.read()

    # 调用七牛上传图片
    try:
        file_name = storage(image_data)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.THIRDERR, errmsg='上传图片失败')

    # 保存头像地址到数据库中
    try:
        User.query.filter_by(id=user_id).update({"avatar_url": file_name})
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='保存图片失败')

    # 头像的七牛地址
    avatar_url = constants.QINIU_URL_DOMAIN + file_name

    # 返回结果
    return jsonify(errno=RET.OK, errmsg='上传图片成功', data={'avatar_url': avatar_url})


@api.route('/users/name', methods=['PUT'])
@login_required
def change_user_name():
    """修改用户名"""
    user_id = g.user_id
    req_data = request.get_json()

    # 判断参数的完整性
    if req_data is None:
        return jsonify(errno=RET.PARAMERR, errmsg='参数不完整')

    # 获取要修改的name值
    name = req_data.get('name')

    # 判断是否为空
    if not name:
        return jsonify(errno=RET.PARAMERR, errmsg='用户名不能为空')

    # 保存用户名到数据库（更新操作），同时利用数据库的唯一索引判断是否重复
    try:
        User.query.filter_by(id=user_id).update({"name": name})
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='设置用户名错误')

    # 更新session中的name值
    session['name'] = name

    # 返回结果
    return jsonify(errno=RET.OK, errmsg='修改成功')


@api.route('/user', methods=['GET'])
@login_required
def get_user_profile():
    """个人主页中获取用户信息
    包括：用户头像，手机号，用户名
    要求：json格式
    """
    # 获取用户id
    user_id = g.user_id

    # 根据用户id查询该用户的信息
    try:
        user = User.query.get(user_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='获取用户信息失败')

    # 判断获取的user是否为空
    if user is None:
        jsonify(errno=RET.NODATA, errmsg='无效操作')

    return jsonify(errno=RET.OK, errmsg='OK', data=user.to_dict())


@api.route('/users/auth', methods=['GET'])
@login_required
def get_user_auth():
    """获取用户的实名认证信息"""
    user_id = g.user_id

    try:
        user = User.query.get(user_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='获取用户实名信息失败')

    if user is None:
        return jsonify(errno=RET.NODATA, errmsg='无效操作')

    return jsonify(errno=RET.OK, errmsg='OK', data=user.auto_to_dict())


@api.route('/users/auth', methods=['POST'])
@login_required
def set_user_auth():
    """保存实名认证信息
    包括：真实名、身份证号
    要求：json格式
    """
    # 获取用户id
    user_id = g.user_id

    # 获取实名信息
    req_data = request.get_json()

    if not req_data:
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')

    real_name = req_data.get('real_name')
    id_card = req_data.get('id_card')

    # 判断参数的完整性
    if not all([real_name, id_card]):
        return jsonify(errno=RET.PARAMERR, errmsg='参数不完整')

    try:
        User.query.filter_by(id=user_id, real_name=None, id_card=None).update({"real_name": real_name, "id_card": id_card})
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(errno=RET.DBERR, errmsg='保存实名信息失败')

    # 返回结果
    return jsonify(errno=RET.OK, errmsg='OK')



