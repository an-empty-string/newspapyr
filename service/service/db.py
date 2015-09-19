from peewee import *
from service import app
from service.config import config

db_config = config["database"]
db = PostgresqlDatabase(db_config["db"], user=db_config["user"], host=db_config["host"])

@app.before_request
def before_request_handler():
    db.connect()

@app.after_request
def after_request_handler():
    db.close()

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(32)
    password = CharField(60)

class Article(BaseModel):
    title = CharField(8192)
    source = CharField(128)
    time = DateTimeField()
    text = TextField()

class Keyword(BaseModel):
    word = CharField(128)

class ArticleKeyword(BaseModel):
    article = ForeignKeyField(Article, related_name='articlekeywords')
    keyword = ForeignKeyField(Keyword, related_name='articlekeywords')

class ArticleKeywordVote(BaseModel):
    user = ForeignKeyField(User, related_name='articlekeywordvotes')
    article_keyword = ForeignKeyField(ArticleKeyword, related_name='votes')
    score = IntegerField()

class ArticleVote(BaseModel):
    user = ForeignKeyField(User, related_name='articlevotes')
    article = ForeignKeyField(Article, related_name='uservotes')
    score = IntegerField()
