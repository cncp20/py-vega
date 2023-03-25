from db.user_dao import UserDao

class UserService:
    __user_dao = UserDao()
    
    def login(self, username, password):
        result = self.__user_dao.login(username, password)
        return result
    
    def get_user_role(self, username):
        result = self.__user_dao.search_user_role(username)
        return result
    
    def insert_user(self, username, password, email, role_id):
        self.__user_dao.insert_user(username, password, email, role_id)