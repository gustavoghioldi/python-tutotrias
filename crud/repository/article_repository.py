from services.db_connection_service import DBConnection
from models.article_model import ArticleModel

class ArticleRepository:
    def __init__(self, article_model) -> None:
        self.__article_model = article_model
        self.__db = DBConnection()

    def create(self):
        query = f'INSERT INTO master VALUES ( {self.__article_model.id}, "{self.__article_model.name}",{self.__article_model.qt})'
        print(query)
        self.__db.excecute_sql(query)   
    
    def read(self):
        query = f'SELECT * FROM master' 
        if not self.__article_model.id is None:
            query = f'SELECT * FROM master WHERE id={self.__article_model.id}'
        self.__db.excecute_sql(query)
        cursor = self.__db.get_cursor()
        models = []
        for a in cursor.fetchall():
            models.append(ArticleModel(a[0], a[1], a[2]))
        return models  
