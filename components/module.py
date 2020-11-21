class Module(object):
    """各个类别的组件的父类"""
    __classify__ = {}
    __endpoints__ = {}
    def set_classify(cls,k,v):
        k = k.capitalize()
        if k not in cls.__classify__:
            cls.__classify__[k] = v
        return cls.get_classify(cls,k)

    def get_classify(cls,k):
        return cls.__classify__.get(k.capitalize(),False)


    def set_endpoint(cls,k,v):
        if k not in cls.__endpoints__:
            cls.__endpoints__[k] = v
        return cls.get_endpoint(cls,k)

    def get_endpoint(cls,k):
        return cls.__endpoints__.get(k,False)