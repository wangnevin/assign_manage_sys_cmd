from db.redis_db import pool
import redis

class RedisAssignDao:
    def delete_cache(self, id):
        try:
            con = redis.Redis(connection_pool=pool)
            con.delete(id)
        except Exception as e:
            print(e)
        finally:
            del con

    def cache_assign(self, id, title, student, type, content, create_time):
        try:
            con = redis.Redis(connection_pool=pool)
            con.hmset(id, {"title":title, "student":student, "type":type, "content":content, "create_time":create_time})
            con.expire(id, 7*24*60*60)
        except Exception as e:
            print(e)
        finally:
            del con
