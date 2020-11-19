import functools
import types
class Module(object):
    """
    模块管理类
    """
    @classmethod
    def set_instance_method(cls, func_name,func):
        @functools.wraps(func)
        @staticmethod
        def dummy(*args, **kwargs):
            return func(*args, **kwargs)
        setattr(cls, func_name, dummy)

    @classmethod
    def define(cls,method_name,method_define):
        namespace = {"_method":None}
        method = method_define +"""\n_method = %s""" % method_name
        exec(method,namespace)
        Module.set_instance_method(method_name,namespace["_method"])
        return cls