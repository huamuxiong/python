#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis


class Config(object):
    """基础配置信息"""
    SECRET_KEY = "js@dhfkjbkjfbsjdfg2"

    # 数据库
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root3306@127.0.0.1:3306/ihome-python04"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # flask-session 配置  详细参见：https://pythonhosted.org/Flask-Session/
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True  # 对cookie中的session_id设置隐藏处理
    PERMANENT_SESSION_LIFETIME = 86400  # session数据的有效期，单位：秒


class DevelopmentConfig(Config):
    """开发者模式的配置信息"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境的配置信息"""
    pass


# 映射关系
config_map = {
    "develop": DevelopmentConfig,
    "product": ProductionConfig,
}
