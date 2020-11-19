from functools import wraps
import inspect
import requests
import json


def client(classify, name='', route='', import_model=[], version='base', url="http://127.0.0.1:5000/register/client",
           **options):
    _classify = classify
    _name = name
    _route = route
    _version = version
    _import_model = import_model

    def decorator(func):
        name = func.__code__.co_name if not _name else _name
        route = _classify + '/' + _name + '/' + _version if not _route else _route

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
                req = {
                    "name": name,
                    "doc": inspect.getdoc(func),
                    "code": inspect.getsource(func),
                    "import_model": _import_model,
                    "return_type": type(res).__name__,
                    "argument": func.__code__.co_varnames,
                    "version": version,
                    "classify": classify,
                    "route": route,
                }
                if json.loads(requests.post(url=url, json=req).text)['code'] != 200:
                    raise Exception
                return res
            except Exception as e:
                raise Exception

        return wrapper

    return decorator


@client(classify="xixixi", name='mimimi', version='base')
def test(a, b, c, d=0):
    """
    dsadas
    :param a:
    :param b:
    :param c:
    :param d:
    :return:
    """
    print(a, b, c, d)
    return a, b, c, d


a = 1
test(1, a, 3)
