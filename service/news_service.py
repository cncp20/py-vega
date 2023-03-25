from db.news_dao import NewsDao

class NewsService:
    __news_dao = NewsDao()
    
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