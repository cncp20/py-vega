from mongo_db import client
from gridfs import GridFS
import math
from bson.objectid import ObjectId
# client.school.teacher.insert_one({"name": "test1"})
# client.school.teacher.insert_many(
#     [
#         {"name": "test2"},
#         {"name": "test3"}
#     ]
# )

# result = client.school.teacher.find({})
# for one in result:
#     print(one["name"])

# result = client.school.teacher.find_one({"name": "test1"})
# print(result["name"])

# client.school.teacher.update_many({}, {"$set": {"role": ["班主任"]}})
# client.school.teacher.update_one({"name": "test1"}, {"$set": {"sex": "男"}})
# client.school.teacher.update_one({"name": "test1"}, {"$push": {"role": "xxx"}})

# db = client.school
# gfs = GridFS(db, collection="book")
# file = open("G:/图书馆/产品思维.pdf", "rb")
# args = {"type": "PDF", "keyword": "chanping"}
# gfs.put(file, filename="产品思维.pdf", **args)
# file.close()

# db = client.school
# gfs = GridFS(db, collection="book")
# book = gfs.find_one({"filename": "产品思维.pdf"})
# print(book.filename)
# print(math.ceil(book.length/1024/1024))
 
# db = client.school
# gfs = GridFS(db, collection="book")
# document = gfs.get(ObjectId("xxx"))
# file = open("G:/图书馆/产品思维.pdf", "wb")
# file.write(document.read())
# file.close()

db = client.school
gfs = GridFS(db, collection="book")
gfs.delete(ObjectId("xxx"))
