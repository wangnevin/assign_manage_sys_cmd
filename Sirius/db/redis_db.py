import redis

try:
    pool = redis.ConnectionPool(
        host="localhost",
        port="6379",
        password="3687379",
        db=2,
        max_connections=20
    )
except Exception as e:
    print(e)
