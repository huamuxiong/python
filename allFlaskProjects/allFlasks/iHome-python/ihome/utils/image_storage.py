#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 图片对象存储

# flake8: noqa

from qiniu import Auth, put_data, etag
import qiniu.config

# 需要填写你的 Access Key 和 Secret Key
access_key = '0JJmZK8kJJBD967JKCO1G249SURKrkKoDnodDqt_'
secret_key = 'MfUi5vMyQ4M6uJrpnHa-SFjXihaC_-gQG_b4kOqM'

def storage(file_data):
    """
    上传文件到七牛服务器
    :param file_data: 要上传的文件数据
    :return:
    """

    # 构建鉴权对象
    q = Auth(access_key, secret_key)

    # 要上传的空间
    bucket_name = 'ihome-python04'

    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, None, 3600)

    # 要上传文件的本地路径
    localfile = './sync/bbb.jpg'

    ret, info = put_data(token, None, file_data)
    # print(info)
    # print('*'*10)
    # print(ret)
    # _ResponseInfo__response: < Response[200] >, exception: None, status_code: 200, text_body: {
    #     "hash": "Fs6FFmVNeZgFsLgLgcQcAJMvQ6a9",
    #     "key": "Fs6FFmVNeZgFsLgLgcQcAJMvQ6a9"}, req_id: dO8AAAA9CfilaLoV, x_log: X - Log
    # ** ** ** ** **
    # {'hash': 'Fs6FFmVNeZgFsLgLgcQcAJMvQ6a9', 'key': 'Fs6FFmVNeZgFsLgLgcQcAJMvQ6a9'}
    if info.status_code == 200:
        # 上传成功,返回图片的名字key
        return ret.get('key')
    else:
        # 上传失败，抛出异常
        raise Exception('上传七牛失败')

# if __name__ == '__main__':
#     with open('./1.png', 'rb') as f:
#         file_data = f.read()
#         storage(file_data)


