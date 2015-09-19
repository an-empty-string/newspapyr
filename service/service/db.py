from peewee import *
from service import app
from service.config import config

db_config = config["database"]
db = PostgresqlDatabase(db_config["db"], user=db_config["user"], host=db_config["host"])

@app.before_request
def before_request_handler():
    db.connect()

@app.after_request
def after_request_handler(exc):
    db.close()
    return exc

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(32)
    password = CharField(60)

class Issue(BaseModel):
    title = CharField(8192)
    source = CharField(128)
    time = DateTimeField()
    text = TextField()

class Keyword(BaseModel):
    word = CharField(128)

class IssueKeyword(BaseModel):
    issue = ForeignKeyField(Issue, related_name='issuekeywords')
    keyword = ForeignKeyField(Keyword, related_name='issuekeywords')
