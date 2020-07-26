from db.mysql_assign_dao import MysqlAssignDao
from db.mongo_assign_dao import MongoAssignDao
from db.redis_assign_dao import RedisAssignDao
from db.mysql_user_dao import MysqlUserDao

class AssignService:
    __mysql_assign_dao = MysqlAssignDao()
    __mongo_assign_dao = MongoAssignDao()
    __redis_assign_dao = RedisAssignDao()
    __mysql_user_dao = MysqlUserDao()

    def insert(self, title, student, type_id, content):
        student_id = self.__mysql_user_dao.search_id(student)
        self.__mongo_assign_dao.insert(title, student, content)
        content_id = self.__mongo_assign_dao.search_id(content)
        self.__mysql_assign_dao.insert(title, student_id, type_id, content_id)

    def search_list(self, page):
        result = self.__mysql_assign_dao.search_list(page)
        return result

    def search_count_page(self):
        count_page = self.__mysql_assign_dao.search_count_page()
        return count_page

    def search_unreview_list(self, page):
        result = self.__mysql_assign_dao.search_unreview_list(page)
        return result

    def search_unreview_count_page(self):
        count_page = self.__mysql_assign_dao.search_unreview_count_page()
        return count_page

    def update(self, id, title, type_id, content):
        content_id = self.__mysql_assign_dao.search_content_id(id)
        self.__mongo_assign_dao.update(content_id, title, content)
        self.__mysql_assign_dao.update(id, title, type_id, content_id)

    def delete_cache(self, id):
        self.__redis_assign_dao.delete_cache(id)

    def search_content_id(self, id):
        content_id = self.__mysql_assign_dao.search_content_id(id)
        return content_id

    def get_content(self, content_id):
        content = self.__mongo_assign_dao.get_content(content_id)
        return content

    def update_unreview_assign(self, id):
        self.__mysql_assign_dao.update_unreview_assign(id)

    def cache_assign(self, id, title, student, type, content, create_time):
        self.__redis_assign_dao.cache_assign(id, title, student, type, content, create_time)

    def delete_assign(self, id):
        content_id = self.__mysql_assign_dao.search_content_id(id)
        self.__mysql_assign_dao.delete_assign(id)
        self.__mongo_assign_dao.delete_assign(content_id)
