from db.type_dao import TypeDao

class TypeService:
    __type_dao = TypeDao()
    def search_list(self):
        result = self.__type_dao.search_list()
        return result