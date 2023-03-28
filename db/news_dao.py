from db.mysql_db import pool

class NewsDao:
    def get_unreview_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT n.id, n.title, t.type, u.username FROM t_news n JOIN t_type t ON n.type_id = t.id " \
            "JOIN t_user u ON n.editor_id = u.id WHERE n.state = %s " \
            "ORDER BY n.create_time DESC " \
            "LIMIT %s, %s"
            cursor.execute(sql, ("待审批", (page - 1) * 10, 10))
            list = cursor.fetchall()
            return list
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
    
    def get_unreview_count(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT CEIL(COUNT(*)/10) FROM t_news WHERE state=%s"
            cursor.execute(sql, ("待审批",))
            count = cursor.fetchone()[0]
            return count
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
        
    def update_unreview_news(self, id):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            con.start_transaction()
            sql = "UPDATE t_news SET state=%s WHERE id=%s"
            cursor.execute(sql, ("已审批", id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()
                
    def get_all_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT n.id, n.title, t.type, u.username FROM t_news n JOIN t_type t ON n.type_id = t.id " \
            "JOIN t_user u ON n.editor_id = u.id " \
            "ORDER BY n.create_time DESC " \
            "LIMIT %s, %s"
            cursor.execute(sql, ((page - 1) * 10, 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
    
    def get_all_count(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT CEIL(COUNT(*)/10) FROM t_news"
            cursor.execute(sql)
            count = cursor.fetchone()[0]
            return count
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
                
    def delete_news(self, id):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            con.start_transaction()
            sql = "DELETE FROM t_news WHERE id=%s"
            cursor.execute(sql, (id,))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()
                
    def insert(self, title, editor_id, type_id, content_id, is_top):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            con.start_transaction()
            sql = "INSERT INTO t_news(title, editor_id, type_id, content_id, is_top, state) " \
                "VALUES(%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, (title, editor_id, type_id, content_id, is_top, "待审批"))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()
    
    def search_cache(self, id):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT n.title, u.username, t.type, n.content_id, n.is_top, n.create_time " \
                "FROM t_news n " \
                "JOIN t_type t ON n.type_id = t.id " \
                "JOIN t_user u ON n.editor_id = u.id " \
                "WHERE n.id = %s"
            cursor.execute(sql, (id,))
            result = cursor.fetchone()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
                
    def search_by_id(self, id):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT n.title, t.type, n.is_top " \
                "FROM t_news n " \
                "JOIN t_type t ON n.type_id = t.id " \
                "WHERE n.id = %s"
            cursor.execute(sql, (id,))
            result = cursor.fetchone()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
                
    def update_news(self, id, title, type_id, content_id, is_top):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            con.start_transaction()
            sql = "UPDATE t_news SET title=%s, type_id=%s, content_id=%s, is_top=%s, state=%s, update_time=NOW() WHERE id=%s"
            cursor.execute(sql, (title, type_id, content_id, is_top, "待审批", id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()