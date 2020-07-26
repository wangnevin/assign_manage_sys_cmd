from db.mysql_db import pool
import math

class MysqlAssignDao:
    def insert(self, title, student_id, type_id, content_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "INSERT INTO t_assign(title, student_id, type_id, content_id, state) " \
                  "VALUES(%s, %s, %s, %s, %s);"
            cursor.execute(sql, (title, student_id, type_id, content_id, '待审批'))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def search_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT a.id,a.title,t.type,u.username FROM t_assign a " \
                  "JOIN t_user u ON a.student_id=u.id " \
                  "JOIN t_type t ON a.type_id=t.id " \
                  "LIMIT %s,%s;"
            cursor.execute(sql, ((page-1)*10, 10))
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
            sql = "SELECT COUNT(*) FROM t_assign;"
            cursor.execute(sql)
            result = math.ceil(cursor.fetchone()[0]/10)
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def search_unreview_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT a.id,a.title,t.type,u.username FROM t_assign a " \
                  "JOIN t_user u ON a.student_id=u.id " \
                  "JOIN t_type t ON a.type_id=t.id " \
                  "WHERE a.state=%s LIMIT %s,%s;"
            cursor.execute(sql, ("待审批", (page-1)*10, 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def search_unreview_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT COUNT(*) FROM t_assign WHERE state=%s;"
            cursor.execute(sql, ["待审批"])
            result = math.ceil(cursor.fetchone()[0]/10)
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def update(self, id, title, type_id, content_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "UPDATE t_assign SET title=%s,type_id=%s,content_id=%s,update_time=NOW(),state=%s WHERE id=%s;"
            cursor.execute(sql, (title, type_id, content_id, '待审批', id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def search_content_id(self, id):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT content_id FROM t_assign WHERE id=%s;"
            cursor.execute(sql, [id])
            result = cursor.fetchone()[0]
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def update_unreview_assign(self, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "UPDATE t_assign SET update_time=NOW(),state=%s WHERE id=%s;"
            cursor.execute(sql, ('已审批', id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def delete_assign(self, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "DELETE FROM t_assign WHERE id=%s;"
            cursor.execute(sql, [id])
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

