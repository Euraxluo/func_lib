import functools
from components.client import client
from components.module import Module
class Manage(object):
    @classmethod
    def set_instance_method(cls,classify_cls,data,func):
        """自动定义类并注入实例"""
        method_name = data['func_name']
        @functools.wraps(func)
        @staticmethod
        def dummy(*args, **kwargs):
            return func(*args, **kwargs)
        setattr(classify_cls, method_name, dummy)
        if method_name not in classify_cls.__dict__:
            raise Exception
        return True

    @classmethod
    def define(cls,data):
        """根据定义实例化代码,然后注入到相应的分类对应的类中"""
        if data['import_model']:
            for pkgs in data['import_model'].split('|'):
                pkg = pkgs.split(' ')[1]
                Manage.install_and_import(pkg)
        namespace = {"_method":None,"client":client}
        method = """%s\n""" % data['import_model'] +data['code'] +"""\n_method = %s""" % data['func_name']
        exec(method,namespace)
        classify_cls = cls.build_cls(data)
        if not classify_cls:
            raise Exception
        return cls.set_instance_method(classify_cls,data, namespace["_method"])

    @classmethod
    def build_cls(cls,data):
        """定义类别类"""
        if data['classify'].capitalize() not in cls.__dict__:
            classify_cls = type(data['classify'].capitalize(),(Module,),{"__classify__":data['classify']})
            Module.set_classify(Module,data['classify'].capitalize(),classify_cls)
        return Module.get_classify(Module,data['classify'].capitalize())

    @staticmethod
    def install_and_import(package):
        import importlib
        try:
            importlib.import_module(package)
        except ImportError:
            import pip
            pip.main(['install', package])
        finally:
            globals()[package] = importlib.import_module(package)