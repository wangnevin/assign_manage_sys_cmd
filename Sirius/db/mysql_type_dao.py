from db.mysql_db import pool

class MysqlTypeDao:
    def search_list(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT * FROM t_type;"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
