import sys
from models.article_model import ArticleModel
from repository.article_repository import ArticleRepository

def read (id_art: int):
    am = ArticleModel(id_art, None, None)
    ar = ArticleRepository(am)
    for m in ar.read():
        print(m.__dict__)

if len(sys.argv) < 2:
    read(None)
else:
    read(sys.argv[1])  
