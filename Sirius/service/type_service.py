from db.mysql_type_dao import MysqlTypeDao

class TypeService:
    __mysql_type_dao = MysqlTypeDao()

    def search_list(self):
        result = self.__mysql_type_dao.search_list()
        return result
