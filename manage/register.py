import json
from flask import request
from manage import register_route as register
from repository.component import Component,session

@register.route("/client",methods=['post'])
def client():
    """代码实例生成"""

    try:
        data = request.get_json()
        # 创建session对象:
        # 创建新User对象:
        new_component = Component(**data)
        print(new_component)
        # 添加到session:
        session.add(new_component)
        # 提交即保存到数据库:
        session.commit()
        # 关闭session:
        session.close()
        return {"code": 200, "mesage": "Ok"}
    except Exception as e:
        raise e

    # rpi_function_define = json.loads(restful_rpi)['function_define']
    # foo_result = Module.define('foo',rpi_function_define).foo(**data)
    # print(foo_result)
    # return {"restful_rpc":restful_rpc,'restful_rpi':foo_result}


@register.route("/test")
def test():
    return "<h1>TEST<h1>"



