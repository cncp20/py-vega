from db.mongo_db import client
from bson.objectid import ObjectId

class MongoNewsDao:
    def insert(self, title, content):
        try:
            client.vega.news.insert_one({
                "title": title,
                "content": content
            })
        except Exception as e:
            raise e
        
    def search_id(self, title):
        try:
            news = client.vega.news.find_one({"title": title})
            return str[news["_id"]]
        except Exception as e:
            raise e
        
    def update(self, id, title, content):
        try:
            client.vega.news.update_one({"_id": ObjectId(id)}, {"$set": {"title": title, "content": content}})
        except Exception as e:
            raise e
        
    def search_content_by_id(self, id):
        try:
            result = client.vega.news.find_one({"_id": ObjectId(id)})
            return result["content"]
        except Exception as e:
            raise e
        
    def delete_by_id(self, id):
        try:
            client.vega.news.delete_one({"_id": ObjectId(id)})
        except Exception as e:
            raise e