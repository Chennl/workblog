#pip install redis
#https://www.nextofwindows.com/allow-server-running-inside-wsl-to-be-accessible-outside-windows-10-host
import redis
from datetime import datetime
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool = pool)
r.set('foo','bar')
r.set('id',3301061975)
r.set('today',datetime.today().timestamp())
r.delete('foo')
print(r.keys())
print(r.dbsize())

'''
采用pipeline方式
一次性批量提交命令
'''
p = r.pipeline()
p.set('k3', 'v3')
p.set('k4', 'v4')
p.incr('num')
p.incr('num')
p.execute()
print(r.get('num'))

if r.exists('id'):
    print(r.type('id'),r.get('id'))

r.randomkey()
r.keys('k*')

r.set('token','12345678')
r.expire('token',30)
r.ttl('token') 

r.setex('token',30,'12345678')



import random
import string
GAME_BOARD_KEY = 'game.board'
for i in range(1000):
    score =round(random.random()*100)
    user_id =''.join(random.sample(string.ascii_letters,6))
    #随机生成1000个用户，每个用户具有得分和用户名字，插入Redis的有序集合中
    r.zadd(GAME_BOARD_KEY, {user_id:score} )

# 随机获得一个用户和他的得分
user_id, score = r.zrevrange(GAME_BOARD_KEY, 0, -1,withscores=True)[random.randint(0, 200)]
print (user_id, score)

#用有序集合的ZCOUNT获取0-100的个数也就是所有人的数量，获取0-score分数段的人数，也就是这个用户分数超过了多少人
board_count = r.zcount(GAME_BOARD_KEY, 0, 100)
current_count = r.zcount(GAME_BOARD_KEY, 0, score)

print (current_count, board_count)

#取TOP N操作（排行榜应用）
#用有序集合的ZREVRANGEBYSCORE返回指定区间的元素
#ZREVRANGEBYSCORE key max min [WITHSCORES] [LIMIT offset count]
print ('TOP 10')
print ('-' * 20)
for user_id, score in r.zrevrangebyscore(GAME_BOARD_KEY, 100, 0, start=0, num=10, withscores=True):
    print (user_id, score)


#Redis非常适合用来做计数器：就是INCR，DECR，INCRBY


# 实时统计：
# Redis的位图提供了二进制操作，非常适合存储布尔类型的值，常见场景就是记录用户登陆状态。

# 该场景用二进制的方式表示用户是否登录，比如说有10个用户，则0000000000表示无人登录，0010010001表示第3个、第6个、第10个用户登录过，即是活跃的。
# 用到Redis字符串（String）结构中的：BITCOUNT，GETBIT，BITOP命令
# 对本月每天的用户登录情况进行统计，会针对每天生成key，例如今天的：account:active:2016:11:23，也会生成月的key:account:active:2016:11和年的key：key:account:active:2016
# 每个key中的字符串长度就是人数（可能有的key的str没有那么长，那是因为最后一个bit没有set成1，不过没有就相当于是0）

import time
import random
from datetime import datetime

ACCOUNT_ACTIVE_KEY = 'account:active'

r.flushall()
# r.delete(ACCOUNT_ACTIVE_KEY)
now = datetime.utcnow()



def record_active(account_id, t=None):
    #第一次t自己生成，后面t接受传入的年月日
    if t is None:
        t = datetime.utcnow()
    #Redis事务开始
    p = r.pipeline()
    key = ACCOUNT_ACTIVE_KEY
    #组合了年月日三种键值，同时将三个键值对应字符串的account_id位置为1
    #符合逻辑：该人在这一天登陆，肯定也在当前月登陆，也在当年登陆
    for arg in ('year', 'month', 'day'):
        key = '{}:{}'.format(key, getattr(t, arg))
        p.setbit(key, account_id, 1)
    #Redis事务提交，真正执行
    p.execute()

def gen_records(max_days, population, k):
#循环每天的情况，从1-max_days天
    for day in range(1, max_days):
        time_ = datetime(now.year, now.month, day)
        #每天随机生成k个数字，表示k个人活跃
        accounts = random.sample(range(population), k)
        #将这k个人对应在当天的字符串中修改，对应位置的bit置为1，表明这个天他有登陆过
        for account_id in accounts:
            record_active(account_id, time_)
#查看记录100万数据中随机选择10万活跃用户时的内存占用
def calc_memory():
    r.flushall()
#执行前先看当前的内存占用
    print ('USED_MEMORY: {}'.format(r.info()['used_memory_human']))
    start = time.time()
#100万种选择10万，20天
    gen_records(21, 1000000, 100000)
#记录话费时间
    print ('COST: {}'.format(time.time() - start))
#添加记录后的内存占用
    print ('USED_MEMORY: {}'.format(r.info()['used_memory_human']))
