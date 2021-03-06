import json
from flask import request
from manage import register_route as register
import datetime
from repository.component import Component,session
from components.manage import Manage
from conf import REGISTER_CLIENT_ROUTE

@register.route("/client",methods=['post'])
def client():
    """服务端的注册中心"""
    try:
        data = request.get_json()
        data['import_model'] = '|'.join(data['import_model'])
        data['argument'] = '|'.join(data['argument'])
        if storage(data) and rebuild(data):
            return {"code": 200, "message": "Ok"}
        else:
            return {"code": 203, "message": "storage or rebuild faild" }
    except Exception as e:
        print(e)
        raise Exception

def storage(data):
    """存储传过来的参数"""
    try:
        data['update_time'] = datetime.datetime.now()
        new_component = Component(**data)
        old_version = session.query(Component).filter(Component.route == data['route']).filter(
            Component.version == data['version']).order_by(Component.update_time).first()
        if old_version:
            data['create_time'] = old_version.create_time
            session.query(Component).filter(Component.route == data['route']).filter(
                Component.version == data['version']).update(data)
        else:
            session.add(new_component)
        session.commit()
        session.close()
        return True
    except Exception as e:
        print(Exception)
        raise Exception

def rebuild(data):
    """重建传过来的函数"""
    try:
        return Manage.define(data)
    except Exception as e:
        print(Exception)
        raise Exception



def build_from_database():
    funcs = session.query(Component).group_by(Component.route).order_by(Component.update_time).all()
    for func in funcs:
        rebuild(func.__dict__)