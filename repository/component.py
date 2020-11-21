from sqlalchemy import Column, String, Integer, DateTime, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime
from conf import DATABASE_URL

engine = create_engine(DATABASE_URL)
# 创建对象的基类:
Base = declarative_base()

class Component(Base):
    """组件ORM"""
    __tablename__ = 'component'

    id = Column(Integer, primary_key=True, autoincrement=True)  # 主键
    name = Column(String)  # 名字 给路由中心的名字
    func_name = Column(String)  # 函数名字
    doc = Column(String)  # 注释
    code = Column(String)  # 函数定义
    import_model = Column(String)  # 导入的包
    argument = Column(String)  # 参数
    return_type = Column(String)  # 返回类型
    version = Column(String)  # 版本
    classify = Column(String)  # 分类
    route = Column(String)  # 路由
    create_time = Column(DateTime, default=datetime.datetime.now) #创建时间
    update_time = Column(DateTime, default=datetime.datetime.now) #更新时间
    def __repr__(self):
        return f"<Component (name={self.name},argument={self.argument},return_type={self.return_type},version={self.version},classify={self.classify},route={self.route})>"

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
