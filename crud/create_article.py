import sys
from models.article_model import ArticleModel
from repository.article_repository import ArticleRepository

def create (id_art: int, name: str, qt: float ):
    am = ArticleModel(id_art, name , qt)
    ar = ArticleRepository(am)
    ar.create()

create (sys.argv[1], sys.argv[2], sys.argv[3])