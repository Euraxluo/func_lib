from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from conf import DATABASE_URL


engine = create_engine(DATABASE_URL)
# 创建对象的基类:
Base = declarative_base()

class Component(Base):
    # 表的名字:
    __tablename__ = 'component'

    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True)  # 主键
    name = Column(String(20))  # 名字
    doc = Column(String(20))  # 注释
    code = Column(String(20))  # 函数定义
    import_model = Column(String(20))  # 导入的包
    argument = Column(String(20))  # 参数
    return_type = Column(String(20))  # 返回类型
    version = Column(String(20))  # 版本
    classify = Column(String(20))  # 分类
    route = Column(String(20))  # 路由
    def __repr__(self):
        return f"<Component (name={Component.name},argument={Component.argument},return_type={Component.return_type},version={Component.version},classify={Component.classify},route={Component.route})>"

# Create a Schema   生成数据表
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
