from redis_db import pool
import redis


con = redis.Redis(
    connection_pool = pool
)
    
# con.set("city", "伦敦")
# city = con.get("city").decode("utf-8")
# print(city)

# try:
#     con.delete("city")
#     con.mset({"city": "柏林", "country" : "德国"})
#     result = con.mget("country", "city")
#     for one in result:
#         print(one.decode("utf-8"))
# except Exception as e:
#     print(e)
# finally:
#     del con
    
    
# try:
#     con.sadd("employee", 1,2,3)
#     con.srem("empployee", 1)
#     result = con.smembers("employee")
#     for one in result:
#         print(one.decode("utf-8"))
# except Exception as e:
#     print(e)
# finally:
#     del con

# try:
#     con.hmset("9527", {
#         "name": "socket",
#         "gender": "male",
#         "age": "18"                     
#     })
#     flag = con.hexists("9527", "name")
#     print(flag)
#     result = con.hgetall("9527")
#     for one in result:
#         print(one.decode("utf-8"), result[one].decode("utf-8"))
# except Exception as e:
#     print(e)
# finally:
#     del con

# try:
#     pipline = con.pipline()
#     pipline.watch("9527")
#     pipline.multi()
#     pipline.hset("9527", "name", "jack")
#     pipline.execute()
# except Exception as e:
#     print(e)
# finally:
#     if pipline in dir():
#         pipline.reset()
#     del con

# try:
#     result = con.lrange('kill_user', 0, -1)
#     for one in result:
#         print(one.decode("utf-8"))
# except Exception as e:
#     print(e)
# finally:
#     del con
try:
    result = con.hgetall(2)
    print(result)
except Exception as e:
    print(e)
finally:
    del con

