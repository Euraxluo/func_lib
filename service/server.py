import json
from flask import request,jsonify
from components.module import Module
from service import service_route as service


@service.route("/<classify>/<name>/<version>", methods=['POST'])
def dynamic_routing(classify, name, version):
    params = request.get_json()
    route = f"/{classify}/{name}/{version}"
    endpoint = Module.get_endpoint(Module, route)
    if endpoint and classify == endpoint.split('/')[0]:
        func_name = endpoint.split('/')[1]
    else:
        raise Exception
    classify_cls = Module.get_classify(Module, classify)
    if classify_cls and func_name in classify_cls.__dict__:
        func = eval(f"classify_cls.{func_name}")
    else:
        raise Exception
    return jsonify({"code": 200, "classify": classify, "name": name, "version": version, "result": func(**params)})
