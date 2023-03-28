import redis

try:
    pool = redis.ConnectionPool(
        host="localhost",
        port=6379,
        password="",
        db=1,
        max_connections=20
    )
except Exception as e:
    raise e