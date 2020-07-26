from db.mysql_db import pool
import math

class MysqlUserDao:

    def login(self, username, password):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT COUNT(*) FROM t_user WHERE username=%s AND AES_DECRYPT(UNHEX(password), 'HelloWorld')=%s;"
            cursor.execute(sql, (username, password))
            result = cursor.fetchone()[0]
            if result > 0:
                return True
            return False
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def search_id(self, username):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT id FROM t_user WHERE username=%s;"
            cursor.execute(sql, [username])
            user_id = cursor.fetchone()[0]
            return user_id
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def search_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT u.id,u.username,u.email FROM t_user u JOIN t_role r ON u.role_id=r.id " \
                  "WHERE r.role=%s LIMIT %s,%s;"
            cursor.execute(sql, ("学生", (page-1)*10, 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def search_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT COUNT(*) FROM t_user WHERE role_id=%s;"
            cursor.execute(sql, ["2"])
            result = math.ceil(cursor.fetchone()[0]/10)
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def insert(self, username, password, email):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "INSERT INTO t_user SET username=%s, password=HEX(AES_ENCRYPT(%s, 'HelloWorld')), email=%s, role_id=%s;"
            cursor.execute(sql, (username, password, email, '2'))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def update(self, id, username, password, email):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "UPDATE t_user SET username=%s, password=HEX(AES_ENCRYPT(%s, 'HelloWorld')), email=%s, role_id=%s " \
                  "WHERE id=%s;"
            cursor.execute(sql, (username, password, email, '2', id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def delete_user(self, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "DELETE FROM t_user WHERE id=%s;"
            cursor.execute(sql, [id])
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()
