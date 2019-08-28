#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from flask import session, current_app, jsonify, request, g
from datetime import datetime

from . import api
from ihome.models import Area, House, Facility, HouseImage, User, Order
from ihome.utils.response_code import RET
from ihome import db, redis_store, constants
from ihome.utils.commons import login_required
from ihome.utils.image_storage import storage


@api.route('/areas')
def get_area_info():
    """获取区域信息"""

    # 从redis中获取数据
    try:
        resp_json = redis_store.get('area_info')
    except Exception as e:
        current_app.logger.error(e)
    else:
        if resp_json is not None:
            current_app.logger.info('hide redis area_info')
            return resp_json, 200, {"Contant-Type": 'application/json'}
    # 查新数据库
    try:
        area_li = Area.query.all()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='数据库异常')
    area_dict_li = []
    for area in area_li:
        area_dict_li.append(area.to_dict())

    # 将数据转换为json格式
    resp_dict = dict(errno=RET.OK, errmsg='OK', data=area_dict_li)
    resp_json = json.dumps(resp_dict)

    # 将数据保存到redis中
    try:
        redis_store.setex('area_info', constants.AREA_INFO_REDIS_CACHE_EXPIRE, resp_json)
    except Exception as e:
        current_app.logger.error(e)

    return resp_json, 200, {"Contant-Type": 'application/json'}


@api.route('/houses/info', methods=['POST'])
@login_required
def save_house_info():
    """保存房屋的基本信息：发布
    前端发送过来的json数据
    {
        "title": "",
        "price": "",
        "area_id": "",
        "address": "",
        "room_count": "",
        "acreage": "",
        "unit": "",
        "capacity": "",
        "beds": "",
        "deposit": "",
        "min_days": "",
        "max_days": "",
        "facility": ["7", "8"]
    }
    """
    # 获取数据
    user_id = g.user_id

    house_data = request.get_json()

    title = house_data.get('title')  # 标题
    price = house_data.get('price')  # 单价
    area_id = house_data.get('area_id')  # 区域的编号
    address = house_data.get('address')  # 地址
    room_count = house_data.get('room_count')  # 房间数
    acreage = house_data.get('acreage')  # 面积
    unit = house_data.get('unit')  # 布局（几厅几室）
    capacity = house_data.get('capacity')  # 可容纳人数
    beds = house_data.get('beds')  # 卧床数目
    deposit = house_data.get('deposit')  # 押金
    min_days = house_data.get('min_days')  # 最小入住天数
    max_days = house_data.get('max_days')  # 最大入住天数

    # 校验必填参数，facility非必填
    if not all([title, price,area_id,address,room_count,acreage, unit,capacity,beds,deposit,min_days,max_days]):
        return jsonify(errno=RET.PARAMERR, errmsg='参数不完整')

    # 对单价和押金作出判断，是否是数字，判断方法：可否转换成数字
    try:
        price = int(float(price)*100)
        deposit = int(float(deposit)*100)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')

    # 判断城区是否存在，防止发布的城区在数据库中没有，进行过滤操作
    try:
        area = Area.query.get(area_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='数据异常')

    # 如果城区在数据库中不存在
    if area is None:
        return jsonify(errno=RET.NODATA, errmsg='城区信息有误')

    # 其他验证，略

    # 保存数据
    house = House(
        user_id=user_id,
        area_id=area_id,
        title=title,
        price=price,
        room_count=room_count,
        address=address,
        acreage=acreage,
        unit=unit,
        capacity=capacity,
        beds=beds,
        deposit=deposit,
        min_days=min_days,
        max_days=max_days
    )

    # 处理房屋设施信息
    facility_ids = house_data.get('facility')

    # 如果用户勾选了设施信息，再保存到数据库
    if facility_ids:
        # ["7", "8", ..]
        # 过滤出设施数据在数据库中存在的数据
        try:
            facilities = Facility.query.filter(Facility.id.in_(facility_ids)).all()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg='数据库异常')

        if facilities:
            # 表示有合法的设施数据
            # 保存数据库
            house.facilities = facilities
    try:
        db.session.add(house)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(errno=RET.DBERR, errmsg='保存数据错误')

    # 保存数据成功
    return jsonify(errno=RET.OK, errmsg='保存数据成功', data={"house_id": house.id})


@api.route('/houses/image',methods=['POST'])
@login_required
def save_house_image():
    """保存房屋图片
    参数：图片，房屋的id
    """
    image_file = request.files.get("house_image")
    house_id = request.form.get('house_id')

    #验证参数的完整性
    if not all([image_file, house_id]):
        return jsonify(errno=RET.PARAMERR, errmsg='参数不完整')

    # 判断房屋是否存在
    try:
        house = House.query.get(house_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='数据库异常')

    if house is None:
        return jsonify(errno=RET.NODATA, errmsg='房屋不存在')

    # 保存图片到七牛
    image_data = image_file.read()
    try:
        file_name = storage(image_data)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.THIRDERR, errmsg='上传图片失败')

    # 保存图片到数据库
    house_image = HouseImage(house_id=house_id, url=file_name)
    db.session.add(house_image)

    # 处理房屋的主图片
    if not house.index_image_url:
        house.index_image_url = file_name
        db.session.add(house)

    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(errno=RET.DBERR, errmsg='保存图片异常')

    # 返回结果
    image_url = constants.QINIU_URL_DOMAIN + file_name
    return jsonify(errno=RET.OK, errmsg='OK', data={"image_url": image_url})


# GET 127.0.0.1:5000/user/houses

@api.route('/user/houses', methods=['GET'])
@login_required
def get_user_houses():
    """获取房东发布的房源信息条目"""
    user_id = g.user_id

    try:
        user = User.query.get(user_id)
        houses = user.houses
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='获取房信息异常')

    # 将获取的房源信息转换成字典放到列表中
    houses_li = []
    if houses:
        for house in houses:
            houses_li.append(house.to_basic_dict())
    return jsonify(errno=RET.OK, errmsg='OK', data={"houses": houses_li})


# GET 127.0.0.1:5000/houses/index

@api.route("/houses/index", methods=['GET'])
def get_house_index():
    """获取主页幻灯片展示的房屋基本信息"""
    # 从缓存中尝试获取数据
    try:
        ret = redis_store.get("home_page_data")
    except Exception as e:
        current_app.logger.error(e)
        ret = None

    if ret:
        current_app.logger.info('hit house index info redis')
        # 因为redis中保存的是json字符串，所以直接进行字符串拼接返回
        return '{"errno": 0, "errmsg": "OK", "data": %s}' % ret.decode('utf-8'), 200, {"Content-Type": "application/json"}
    else:
        try:
            # 查询数据库，返回房屋订单数目最多的5条数据
            houses = House.query.order_by(House.order_count.desc()).limit(constants.HOME_PAGE_MAX_HOUSES)
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg='查询数据库失败')

        if not houses:
            return jsonify(errno=RET.NODATA, errmsg='查询无数据')

        houses_li = []
        for house in houses:
            # 如果房主为设置主图片，则跳过
            if not house.index_image_url:
                continue
            houses_li.append(house.to_basic_dict())

        # 将数据转换为json数据，并保存到redis中
        json_houses = json.dumps(houses_li)
        try:
            redis_store.setex("home_page_data", constants.AREA_INFO_REDIS_CACHE_EXPIRE, json_houses)
        except Exception as e:
            current_app.logger.error(e)

        return '{"errno": 0, "errmsg": "OK", "data": %s}' % json_houses, 200, {"Content-Type": "application/json"}


# GET 127.0.0.1:5000/api/v1.0/houses/1

@api.route("/houses/<int:house_id>", methods=['GET'])
def get_house_detail(house_id):
    """获取房屋详情页数据"""
    # 前端在房屋详情页面展示时，如果浏览页面的用户不是该房屋的房东，则展示预订按钮，否则不展示
    # 所以需要后端返回登陆用户的user_id
    # 尝试获取用户登陆的信息，若登陆，则返回给前端登陆用户的user_id，否则返回user_id=-1
    user_id = session.get("user_id", "-1")

    # 校验参数
    if not house_id:
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')

    # 先从redis缓存中获取数据
    try:
        ret = redis_store.get("house_info_%s" % house_id)
    except Exception as e:
        current_app.logger.error(e)
        ret = None
    if ret:
        current_app.logger.info('hit house info redis')
        return '{"errno": 0, "errmsg": "OK", "data":{"user_id": %s, "house": %s}}' % (user_id, ret.decode('utf-8')), 200, {"Content-Type1": "application/json"}
    # 查询数据库
    try:
        house = House.query.get(house_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='插叙数据失败')

    if not house:
        return jsonify(errno=RET.NODATA, errmsg='房屋不存在')

    # 将房屋对象数据转换为字典
    try:
        house_data = house.to_full_dict()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg='数据出错')

    # 存入到redis中
    json_house = json.dumps(house_data)
    try:
        redis_store.setex("house_info_%s" % house_id, constants.HOUSE_DETAIL_REDIS_EXPIRE_SECOND, json_house)
    except Exception as e:
        current_app.logger.error(e)

    resp = '{"errno": 0, "errmsg": "OK", "data":{"user_id": %s, "house": %s}}' % (user_id, json_house), 200, {"Content-Type1": "application/json"}
    return resp


# GET 127.0.0.1:5000/api/v1.0/houses?sd=2019-08-16&ed=2019-18-17&aid=1&sk=new&p=1
# 参数分别为：入住时间，结束时间，区域编号，排序，页数

@api.route("/houses", methods=['GET'])
def get_house_list():
    """获取房屋的列表信息（搜索页面）"""

    # 获取参数
    start_date = request.args.get("sd", "")  # 起始时间
    end_date =request.args.get("ed", "")  # 结束时间
    area_id = request.args.get("aid", "")  # 区域编号
    sort_key = request.args.get("sk", "new")  # 排序关键字
    page = request.args.get("p")  # 页数

    print(start_date)

    # 处理时间
    try:
        if start_date:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")

        if end_date:
            end_date = datetime.strptime(end_date, "%Y-%m-%d")

        if start_date and end_date:
            raise start_date <= end_date
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg='日期参数有误')

    # 判断区域 id
    if area_id:
        try:
            area = Area.query.get(area_id)
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.PARAMERR, errmsg='区域参数有误')

    # 处理页数
    try:
        page = int(page)
    except Exception as e:
        current_app.logger.error(e)
        page = 1

    # 获取缓存数据
    redis_key = "house_%s_%s_%s_%s" % (start_date, end_date, area_id, sort_key)
    try:
        resp_json = redis_store.hget(redis_key, page)
    except Exception as e:
        current_app.logger.error(e)
    else:
        if resp_json:
            return resp_json, 200, {"Content-Type": "application/json"}

    # 过滤条件的列表容器
    filter_params = []

    # 填充过滤条件
    # 时间条件
    conflict_orders = None

    try:
        if start_date and end_date:
            # 查询冲突的订单
            conflict_orders = Order.query.filter(
                Order.begin_date <= end_date, Order.end_date >= start_date).all()

        elif start_date:
            # 查询冲突的订单
            conflict_orders = Order.query.filter(Order.end_date >= start_date).all()
        elif end_date:
            # 查询冲突的订单
            conflict_orders = Order.query.filter(Order.begin_date <= end_date).all()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='数据库异常')

    if conflict_orders:
        # 从订单中获取冲突的房子 id
        conflict_house_ids = [order.house_id for order in conflict_orders]

        # 如果冲突的房子id不为空，向查询的参数中添加条件
        if conflict_house_ids:
            filter_params.append(House.id.notin_(conflict_house_ids))

    # 区域条件
    if area_id:
        filter_params.append(House.area_id == area_id)

    # 查询数据库, 加过滤排序条件
    if sort_key == 'booking':
        house_query = House.query.filter(*filter_params).order_by(House.order_count.desc())
    elif sort_key == 'price-inc':
        house_query = House.query.filter(*filter_params).order_by(House.price.asc())
    elif sort_key == 'price-des':
        house_query = House.query.filter(*filter_params).order_by(House.price.desc())
    else:
        house_query = House.query.filter(*filter_params).order_by(House.create_time.desc())

    # 处理分页
    try:
        page_obj = house_query.paginate(page=page, per_page=constants.HOUSE_LIST_PAGE_CAPACITY, error_out=False)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='数据库异常')

    # 获取页面数据
    house_li = page_obj.items
    houses = []
    for house in house_li:
        houses.append(house.to_basic_dict())

    # 获取总页数
    total_page = page_obj.pages

    # 将数据转换成字典保存
    resp_dict = dict(errno=RET.OK, errmsg='OK',data={"total_page": total_page, "houses": houses, "current_page": page})
    # 将字典数据转换成json格式的数据
    resp_json = json.dumps(resp_dict)

    # redis
    # house_起始_结束_区域id_排序：hash
    # {
    #     "1": {},
    #     "2": {},
    # }

    if page <= total_page:
        # 设置缓存数据
        redis_key = "house_%s_%s_%s_%s" % (start_date, end_date, area_id, sort_key)

        # 哈希类型
        try:
            # redis_store.hset(redis_key, page, resp_json)
            # redis_store.expire(redis_key, constants.HOUSE_LIST_PAGE_REDIS_CACHE_EXPIRE)

            # 创建redis管道对象，可以一次执行多个语句
            pipeline = redis_store.pipeline()

            # 开启多个语句的记录
            pipeline.multi()

            redis_store.hset(redis_key, page, resp_json)
            redis_store.expire(redis_key, constants.HOUSE_LIST_PAGE_REDIS_CACHE_EXPIRE)

            # 执行语句
            pipeline.execute()
        except Exception as e:
            current_app.logger.error(e)

    return resp_json, 200, {"Content-Type": "application/json"}





