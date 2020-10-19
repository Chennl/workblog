#models.py
#https://www.osgeo.cn/sqlalchemy/dialects/mysql.html#mysql-data-types
#https://docs.sqlalchemy.org/en/13/orm/self_referential.html#self-referential-query-strategies

from sqlalchemy import Table,Column, Integer, String, Text, DateTime, Float, Boolean,DECIMAL, ForeignKey,func
from sqlalchemy import MetaData
from sqlalchemy.orm import relationship,backref
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
 
class Department(Base):
    __tablename__ = 'demo_department'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    create_date = Column(DateTime,default=func.now())
    employees = relationship('Employee',back_populates='department')

class Address(Base):
    __tablename__ = 'demo_addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String(100), nullable=False)
    employee_id = Column(Integer, ForeignKey('demo_employee.id'))
    employee = relationship('Employee', back_populates="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address

class Employee(Base):
    __tablename__ = 'demo_employee'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    # Use default=func.now() to set the default hiring time
    # of an Employee to be the current time when an
    # Employee record was created
    hired_on = Column(DateTime, default=func.now())
    department_id = Column(Integer, ForeignKey('demo_department.id'),nullable=False)
    remark = Column(String(100),default='')

    department = relationship(Department,back_populates='employees')
        # backref=backref('employees',
        #                  uselist=True,
        #                  cascade='delete,all'))
    addresses = relationship('Address', order_by=Address.id, back_populates="employee")

category_tree = Table(
    'mall_category_tree', 
    Base.metadata,
    Column('parent_id', Integer, ForeignKey('mall_category.id')),
    Column('children_id', Integer, ForeignKey('mall_category.id'))
)

class Node(Base):
    __tablename__ = 'demo_node'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('demo_node.id'))
    data = Column(String(50))
    children = relationship("Node")


class Category(Base):
    '商品分类表'
    __tablename__ = 'mall_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50),nullable=False)
    imgUrl = Column(String(150),nullable=True)
    level = Column(Integer,default=0)
    children_categories = relationship(
        'Category',
        secondary=category_tree,
        primaryjoin =(category_tree.c.parent_id == id),
        secondaryjoin=(category_tree.c.children_id == id),
        backref= backref('parents',lazy='dynamic'),
        lazy='select'
    )
    create_date = Column(DateTime,default=func.now())

    def as_dict(self):
        data = {
                'id':self.id,
                'name':self.name,
                'level':self.level,
                'imgUrl':self.imgUrl,
                'children_categories':[obj.as_dict() for obj in self.children_categories],
                'create_date':self.create_date.strftime('%Y-%m-%d %H:%M:%S')
                }
        return data

class Goods(Base):
    '商品类'
    __tablename__ = 'mall_goods'
    id = Column(Integer, primary_key=True)
    name= Column(String(128)) 
    privilegePrice = Column(DECIMAL(10,2))
    price = Column(DECIMAL(10,2))
    imgUrl = Column(String(256))
    details = Column(String(1024))
    remark= Column(String(128))
    createDate = Column(DateTime, default=func.now())
    updateDate = Column(DateTime, default=func.now())
    clickRate= Column(Integer)
    buyRate= Column(Integer)
    stock= Column(Integer)
    isHot= Column(Integer)
    isNew= Column(Integer)
    classifyId= Column(Integer)
    discount = Column(DECIMAL(10,2))
    activityId= Column(Integer)
    desc= Column(String(128))
    shopGoodsImageList= Column(String(512))

