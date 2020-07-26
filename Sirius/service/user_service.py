from db.mysql_user_dao import MysqlUserDao

class UserService:
    __mysql_user_dao = MysqlUserDao()

    def login(self, username, password):
        result = self.__mysql_user_dao.login(username, password)
        return result

    def search_id(self, username):
        user_id = self.__mysql_user_dao.search_id(username)
        return user_id

    def insert(self, username, password, email):
        self.__mysql_user_dao.insert(username, password, email)

    def search_list(self, page):
        result = self.__mysql_user_dao.search_list(page)
        return result

    def search_count_page(self):
        count_page = self.__mysql_user_dao.search_count_page()
        return count_page

    def update(self, id, username, password, email):
        self.__mysql_user_dao.update(id, username, password, email)

    def delete_user(self, id):
        self.__mysql_user_dao.delete_user(id)
