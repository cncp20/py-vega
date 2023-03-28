from redis_db import pool
import redis
import random

con = redis.Redis(connection_pool = pool)

try:
    con.delete("name")
    con.zadd("name", {"test1": 0, "test2": 0, "test3": 0, "test4": 0, "test5": 0})
    names = ["test1", "test2", "test3","test4", "test5"]
    for index in range(0, 300):
        i = random.randint(0, 4)
        name = names[i]
        con.zincrby("name", 1, name)
    result = con.zrevrange("name", 0, -1, "WITHSCORES")
    for one in result:
        print(one[0].decode("utf-8"), int(one[1]))
except Exception as e:
    raise e
finally:
    del con