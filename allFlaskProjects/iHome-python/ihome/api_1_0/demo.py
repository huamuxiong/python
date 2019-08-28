#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 导入蓝图对象
from . import api
from flask import current_app
from ihome import models


@api.route("/index")
def index():
    current_app.logger.error('dmngdcfnf')
    current_app.logger.warn('dmngdcfnf')
    current_app.logger.info('dmngdcfnf')
    current_app.logger.debug('dmngdcfnf')

    return "index page"

