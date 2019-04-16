#-*- coding:UTF-8 -*-
import pymongo
from pymongo import MongoClient
#连接到数据库系统
#conn = MongoClient('127.0.0.1',27017)
conn = MongoClient('localhost',27017)
#创建数据库
db = conn.lxc
#创建集合，并指定集合类型
myset:pymongo.collection.Collection = db.hunter
# print(type(myset)) #打印集合类型
#增
# myset.insert_one({"name":"red","age":27})
# myset.insert_many([{"name":"wolf","age":27},{"name":"ray","age":16}])
#改
# myset.update_one({'name':'red'},{'$set':{'name':'rw'}})
#删
# myset.delete_one({'name':'rw'}) #删除一个
# myset.delete_many({}) #清空集合
#查
for set_obj in myset.find():
    print(set_obj)
#断开连接
conn.close()












