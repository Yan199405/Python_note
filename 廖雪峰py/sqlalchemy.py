from sqlalchemy import  Column,String,create_engine
from sqlalchemy.orm import  sessionmaker
from sqlalchemy.ext.declarative import  declarative_base

#创建对象的基类：
base = declarative_base()

#定义User对象
class User(Base):
    #表的名字
    __tablename__ = 'usertest'
    #表的结构
    id = Column(String(20),primary_key=True)
    name = Column(String(20))

#初始化数据库链接：
engine = create_engine('mysql+mysqlconnector://root:shcaee.com@211.152.37.10:3306/test')

#创建DBSession类型：
DBSession = sessionmaker(bind=engine)