from db.mysql_role_dao import MysqlRoleDao

class RoleService:
    __mysql_role_dao = MysqlRoleDao()

    def search_role(self, username):
        role = self.__mysql_role_dao.search_role(username)
        return role
