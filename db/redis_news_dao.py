from db.redis_db import pool
import redis

class RedisNewsDao:
    
    def insert(self, id, title, username, type, content, is_top, create_time):
        con = redis.Redis(connection_pool = pool)
        try:
            con.hmset(id, {
                "title": title,
                "author": username,
                "type": type,
                "content": content,
                "is_top": is_top,
                "create_time": create_time
            })
            if is_top == 0:
                con.expire(id, 24 * 60 * 60)
        except Exception as e:
            raise e
        finally:
            if "con" in dir():
                del con
        
    def delete(self, id):
        con = redis.Redis(connection_pool = pool)
        try:
            con.delete(id)
        except Exception as e:
            raise e
        finally:
            if "con" in dir():
                del con