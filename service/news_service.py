from db.news_dao import NewsDao
from db.redis_news_dao import RedisNewsDao

class NewsService:
    __news_dao = NewsDao()
    __redis_news_dao = RedisNewsDao()
    
    def get_unreview_list(self, page):
        result = self.__news_dao.get_unreview_list(page)
        return result
    
    def get_unreview_count(self):
        page_count = self.__news_dao.get_unreview_count()
        return page_count
    
    def update_unreview_news(self, id):
        self.__news_dao.update_unreview_news(id)
        
    def get_all_list(self, page):
        result = self.__news_dao.get_all_list(page)
        return result
    
    def get_all_count(self):
        page_count = self.__news_dao.get_all_count()
        return page_count
    
    def delete_news(self, id):
        self.__news_dao.delete_news(id)
    
    def insert(self, title, editor_id, type_id, content_id, is_top):
        self.__news_dao.insert(title, editor_id, type_id, content_id, is_top)
        
    def cache_news(self, id, title, username, type, content, is_top, create_time):
        self.__redis_news_dao.insert(id, title, username, type, content, is_top, create_time)
        
    def search_cache(self, id):
        result = self.__news_dao.search_cache(id)
        return result
    
    def delete_cache(self, id):
        self.__redis_news_dao.delete(id)
        
    def search_by_id(self, id):
        result = self.__news_dao.search_by_id(id)
        return result
    
    def update_news(self, id, title, type_id, content_id, is_top):
        self.__news_dao.update_news(id, title, type_id, content_id, is_top)
        self.delete_cache(id)