from functools import wraps
import inspect
import requests
import json
from conf import SERVER_URL

def client(classify, name='', route='', import_model=[], version='base', url=SERVER_URL,
           **options):
    """用于客户端的上传装饰器,但是服务端组件管理中心有一个同名的装饰器,只是实现不同"""
    _classify = classify
    _name = name
    _route = route
    _version = version
    _import_model = import_model

    def decorator(func):
        name = func.__code__.co_name if not _name else _name
        route = '/' + _classify + '/' + _name + '/' + _version if not _route else _route
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            try:
                req = {
                    "name": name,
                    "doc": inspect.getdoc(func),
                    "func_name": func.__code__.co_name,
                    "code": inspect.getsource(func),
                    "import_model": _import_model,
                    "return_type": type(res).__name__,
                    "argument": func.__code__.co_varnames,
                    "version": version,
                    "classify": classify,
                    "route": route,
                }
                if json.loads(requests.post(url=url, json=req).text)['code'] != 200:
                    print(f"Exception: request Server faild")
                    return res
                return res
            except Exception as e:
                print(f"Exception: {e}")
                return res
        return wrapper
    return decorator
