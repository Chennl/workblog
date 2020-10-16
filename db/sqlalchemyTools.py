
from sqlalchemy import create_engine,distinct,func,literal
from sqlalchemy import text,and_,or_
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,aliased
from sqlalchemy.sql import exists
from os import environ
import json
import random
import logging
import time

logger = logging.getLogger(__name__)
logging.basicConfig()
logger.setLevel(logging.DEBUG)

Base = declarative_base()
engine = None
session = None

@event.listens_for(Engine, "before_cursor_execute")
def before_cursor_execute(conn, cursor, statement,
                        parameters, context, executemany):
    conn.info.setdefault('query_start_time', []).append(time.time())
    logger.debug("Start Query: %s", statement)

@event.listens_for(Engine, "after_cursor_execute")
def after_cursor_execute(conn, cursor, statement,
                        parameters, context, executemany):
    total = time.time() - conn.info['query_start_time'].pop(-1)
    logger.debug("Query Complete!")
    logger.debug("Total Time: %f", total)

#setup_once
def setup_database(dburl, echo=True,dropall=False):
    global engine
    engine = create_engine(dburl, echo=echo)
    if dropall:
        Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

db_connect_string='mysql+pymysql://root:root@localhost:3306/my753721?charset=utf8'
dburl = environ.get('SQLALCHEMY_DATABASE_URI',db_connect_string)
# 



# Create a session
def make_session():
    global session
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

from db.models import Employee,Department,Category,Goods,Node

def init_employee_data():
    
    
    # with engine.connect() as conn:
    #     result = conn.execute(Department.__table__.delete())
    #     result = conn.execute(Employee.__table__.delete())
    
    # session.execute(Employee.__table__.delete())
    # session.execute(Department.__table__.delete())
      
    session.query(Employee).delete()
    session.query(Department).delete()

    result = session.execute(
        Department.__table__.insert(),
        params =[
                {
                    "id":i,
                    "name":"Department Name %d"%i,
                } for i in range(101,151)
            ],
    )
    session.commit()

    
    for chunk in range(10000,60000,10000):
        session.execute(
            Employee.__table__.insert(),
            params =[
                    {
                        "id":i,
                        "name":"employee Name %d"%i,
                        "department_id":random.randint(101,150)
                    } for i in range(chunk,chunk+10000)
                ],
        )
        session.commit()

def test_orm_full_objects_chunks(n):
    """Load fully tracked ORM objects a chunk at a time using yield_per()."""
    for obj in session.query(Employee).yield_per(1000).limit(n):
        pass



# query = session.query(
#         Department.id,
#         Department.name,
#         Employee.id,
#         Employee.name,
#     )
#join_query = query.join(Employee).join(Department)
#result = query.filter(Employee.department_id==Department.id).all()
#print(result)

def init_category_data():
    c1 = Category(id= 1,name= "个人护理",level=1)
    c1_1 = Category(id= 2,name= "洗护套装",imgUrl="https://h2.appsimg.com/a.appsimg.com/upload/category/2017/11/06/142/62863029-eb85-4d1a-bdf6-8a67fa91ce3b_300x375_80.jpg")
    c1_2 = Category(id= 3,name= "卸妆",imgUrl="https://h2.appsimg.com/a.appsimg.com/upload/category/2017/02/24/134/6d33dac3-8de7-4980-86be-907a112b1ecf_300x375_80.jpg")
    c1_3 = Category(id= 4,name= "护肤套装",imgUrl="https://h2.appsimg.com/a.appsimg.com/upload/category/2018/06/22/46/96f4e409-faaa-487c-ba8e-a2685e07b62c_300x375_80.png")

    c1.children_categories.append(c1_1)
    c1.children_categories.append(c1_2)
    c1.children_categories.append(c1_3)
    
    c2 = Category(id= 5,name= "护肤彩妆",level=1)
    c2_1 = Category(id= 6,name= "面膜",imgUrl="https://h2.appsimg.com/a.appsimg.com/upload/goadmin/2018/06/22/117/15296371356181_300x375_80.png")
    c2_2 = Category(id= 7,name= "面霜",imgUrl="https://h2.appsimg.com/a.appsimg.com/upload/goadmin/2018/06/25/183/15299035136290_300x375_80.png")
    c2_3 = Category(id= 8,name= "晚霜",imgUrl="https://h2.appsimg.com/a.appsimg.com/upload/goadmin/2018/07/06/72/15308438751848_300x375_80.jpg")
    c2_4 = Category(id= 9,name= "香水",imgUrl="https://h2.appsimg.com/a.appsimg.com/upload/category/2018/05/02/31/e94cfce3-b13d-45de-90e9-baaa15263338_300x375_80.png")

    c2.children_categories.append(c2_1)
    c2.children_categories.append(c2_2)
    c2.children_categories.append(c2_3)
    c2.children_categories.append(c2_4)

    c3 = Category(id= 10,name= "母婴",level=1)

    c4 = Category(id= 11,name= "护肤",level=1)
    c4_1= Category(id= 12,name= "气垫bb",imgUrl= "https://h2.appsimg.com/a.appsimg.com/upload/category/2017/11/06/192/4ee9c39f-d28b-4290-bdc1-a309d9d946ac_200x375_80.png")
    c4_2= Category(id= 13,name= "隔离霜",imgUrl= "https://h2.appsimg.com/a.appsimg.com/upload/category/2017/07/26/60/aa1e0147-7e15-43e5-9081-9b209403d9cc_200x375_80.jpg")
    c4_3= Category(id= 14,name= "修容/高光",imgUrl= "https://h2.appsimg.com/a.appsimg.com/upload/category/2018/06/21/32/a23a796f-0243-430f-a439-3c59dcf4f192_200x375_80.png")
    c4_4= Category(id= 15,name= "CC霜",imgUrl= "https://h2.appsimg.com/a.appsimg.com/upload/category/2018/06/21/51/fb6ab09f-e7f0-494f-a29c-a0fab28a8ba1_200x375_80.png")
    c4_5= Category(id= 16,name= "眼影",imgUrl= "https://h2.appsimg.com/a.appsimg.com/upload/category/2018/05/02/34/1fd89259-2a39-4fa0-bc47-f1f7cf7f1693_200x375_80.png")
    c4_6= Category(id= 17,name= "眼妆",imgUrl= "https://h2.appsimg.com/a.appsimg.com/upload/category/2017/07/26/180/315f3336-1d83-4454-b3a9-9f30b666a4cd_200x375_80.jpg")
    c4_7= Category(id= 18,name= "粉饼",imgUrl= "https://h2.appsimg.com/a.appsimg.com/upload/category/2017/07/26/126/4e8ddbf2-d0e5-4509-b34b-2532c58973e8_200x375_80.png")
    c4_8= Category(id= 19,name= "眼唇/卸妆",imgUrl= "https://h2.appsimg.com/a.appsimg.com/upload/category/2018/07/11/117/9840c455-192e-40d8-aaf9-141a42dfb8f4_200x375_80.png")

    c4.children_categories.append(c4_1)
    c4.children_categories.append(c4_2)
    c4.children_categories.append(c4_3)
    c4.children_categories.append(c4_4)
    c4.children_categories.append(c4_5)
    c4.children_categories.append(c4_6)
    c4.children_categories.append(c4_7)
    c4.children_categories.append(c4_8)

    session.add(c1)
    session.add(c2)
    session.add(c3)
    session.add(c4)
    session.commit()

def get_categories():
    data = session.query(Category).filter(Category.level==1).all()
    return data

#init_category_data()
#data = get_categories()
#print(dir(Category))
#fileds = [x for x in dir(Category) if not x.startswith('_') and x != 'metadata']
#print(fileds)
#print(Category.__table__.columns)
#obj=data[0]
#print(obj.as_dict())
 
#json_str = json.dumps(data[0],cls=new_alchemy_encoder(revisit_self = False, fields_to_expand=Category.__table__.columns),ensure_ascii=False)
#print(json_str)
 
#关联
# result = session.query(Category,Goods.name).filter(Category.id==Goods.classifyId).first()
# result = session.query(Category,Goods.name).join(Goods,Category.id==Goods.classifyId).first()
# result = session.query(Category,Goods.name).outerjoin(Goods,Category.id==Goods.classifyId).first()
class test():
    _db_cls = Department
    def _to_filters( self,**filters):
        """
        Will translate filters to sqlalchemy filter.
        This method will also apply user_id restriction if available.
        
        each parameters of the function is treated as an equality unless the
        name of the parameter ends with either "__gt", "__lt", "__ge", "__le",
        "__ne", "__in" ir "__like".
        """

        db_filters = set()
        for key, value in filters.items():
            if key == '__or__':
                db_filters.add(or_(*[and_(*self._to_filters(**sub_filter))
                                        for sub_filter in value]))
            elif key.endswith('__gt'):
                db_filters.add(getattr(self._db_cls, key[:-4]) > value)
            elif key.endswith('__lt'):
                db_filters.add(getattr(self._db_cls, key[:-4]) < value)
            elif key.endswith('__ge'):
                db_filters.add(getattr(self._db_cls, key[:-4]) >= value)
            elif key.endswith('__le'):
                db_filters.add(getattr(self._db_cls, key[:-4]) <= value)
            elif key.endswith('__ne'):
                db_filters.add(getattr(self._db_cls, key[:-4]) != value)
            elif key.endswith('__in'):
                db_filters.add(getattr(self._db_cls, key[:-4]).in_(value))
            elif key.endswith('__like'):
                db_filters.add(getattr(self._db_cls, key[:-6]).like(value))
            elif key.endswith('__ilike'):
                db_filters.add(getattr(self._db_cls, key[:-7]).ilike(value))
            else:
                db_filters.add(getattr(self._db_cls, key) == value)
        return db_filters

def page_query(category_id=None,page=None, page_size=None):
 
    query=session.query(func.count).select_from(Goods).outerjoin(Category,Category.id==Goods.classifyId).filter(Goods.classifyId.isnot(None)).filter(text("clickRate>200"))
    if category_id:
        query=query.filter(Goods.classifyId==category_id)
    
    query=session.query(Goods.id,Goods.name,Goods.clickRate).select_from(Goods).outerjoin(Category,Category.id==Goods.classifyId).filter(Goods.classifyId.isnot(None)).filter(text("clickRate>200"))
 

    query=query.order_by(text('mall_goods.id desc'))
    
    if page_size:
        query = query.limit(page_size)
    if page:
        query=query.offset(page_size*(page -1))

   
    print(query.column_descriptions)
    #whereclause = query.whereclause
    result=query.all()
    print(result)
# from sqlalchemy import func
# stmt = session.query(Category.id.label('id'),func.count('*').label('children_count')).group_by(Category.id).filter(Category.level==1).subquery()
# result = session.query(Category.name,stmt.c.children_count).join(stmt,Category.id==stmt.c.id).order_by(Category.id).all()
# print(result)

# categoryalias=aliased(Category)
# session.query(Category.id.label('id'),func.count('*').label('count')).outerjoin(categoryalias,Category.id).filter(Category.level==1).all()
#print(dumps(obj))
# sbq = session.query(Address.user_id, func.count('*').label('address_count')).group_by(Address.user_id).subquery()
# session.query(User.name, sbq.c.address_count).outerjoin(sbq, User.id==sbq.c.user_id).all()

# node = session.query(Node).filter(Node.data=='root').first()
# n1= Node(data='new')
# node.children.append(n1)
# session.commit()
# print(node)





# a = session.query(func.count(Node.id)).group_by(Node.parent_id).filter(Node.parent_id==1).scalar()
# print(type(a),a)

# a = session.query(distinct(Node.parent_id),func.count(Node.id)).group_by(Node.parent_id).all()
# print(type(a),a)


setup_database(dburl=dburl)
make_session()
#init_employee_data()
#test_orm_full_objects_chunks(40000)

#page_query(page=3,page_size=5)

#d = session.query(Department).get(101)
#e = session.query(Employee).get(10001)
#print(e)


def dinamic_filter(model_class, filter_condition):
    '''
    Return filtered queryset based on condition.
    :param query: takes query
    :param filter_condition: Its a list, ie: [(key,operator,value)]
    operator list:
        eq for ==
        lt for <
        ge for >=
        in for in_
        like for like
        value could be list or a string
    :return: queryset
    '''
    __query = session.query(model_class)
    for raw in filter_condition:
        try:
            key, op, value = raw
        except ValueError:
            raise Exception('Invalid filter: %s' % raw)
        column = getattr(model_class, key, None)

        if not column:
            raise Exception('Invalid filter column: %s' % key)
        if op == 'in':
            if isinstance(value, list):
                filt = column.in_(value)
            else:
                filt = column.in_(value.split(','))
        else:
            try:
                attr = list(filter(lambda e: hasattr(column, e % op), ['%s', '%s_', '__%s__']))[0] % op
            except IndexError:
                raise Exception('Invalid filter operator: %s' % op)
            if value == 'null':
                value = None
            filt = getattr(column, attr)(value)

        __query = __query.filter(filt)
    return __query


#qy = dinamic_filter(Department,[('id', 'eq', 1),('name','like','%part%')])
#print(qy)
def query_demo():
    # 有员工名称类似8888的部门
    result = session.query(Department).filter(Department.employees.any(Employee.name.ilike('%8888'))).all()
    print(result)
    #  查找没有员工的的部门
    stmt = exists().where(Department.id == Employee.department_id)
    result = session.query(Department).filter(~stmt).all()
    print(result)
#统计每部门人数
stmt = session.query(Employee.department_id,func.count('*').label('employees_count')).group_by(Employee.department_id).subquery()
result = session.query(Department.id,stmt.c.employees_count).outerjoin(stmt,Department.id==stmt.c.department_id).order_by(Department.id).all()
print(result)
#assert('')