from service import service_route as server
from components.module import Module

def client(classify, name='', route='', import_model=[], version='base', url="http://127.0.0.1:5000/register/client",
           **options):
    """处理客户端的带过来的函数,主要功能为路由的添加"""
    _classify = classify
    _name = name
    _route = route
    _version = version
    _import_model = import_model
    def decorator(func):
        name = func.__code__.co_name if not _name else _name
        route = '/'+_classify + '/' + _name + '/' + _version if not _route else _route
        endpoint = _classify + '/' +func.__name__
        """需要将route和function联系在一起"""
        if not add_url_rule(route, endpoint, func):
            raise Exception
        return func

    return decorator


def add_url_rule(rule,endpoint, view_func):
    if endpoint:
        assert "." not in endpoint, "Blueprint endpoints should not contain dots"
    if view_func and hasattr(view_func, "__name__"):
        assert (
                "." not in view_func.__name__
        ), "Blueprint view function name should not contain dots"
    return Module.set_endpoint(Module,rule,endpoint)
