import bcrypt

from service import method
from service.db import User

@method("auth.register")
def create_user(args):
    user = args["username"]
    if User.select().where(User.username == user).count():
        return False

    passwd = args["password"]
    hashed_passwd = bcrypt.hashpw(passwd, bcrypt.gensalt())

    return User.create(username=user, password=hashed_passwd).id

@method("auth.login")
def login(args):
    user = args["username"]
    matching = list(User.select().where(User.username == user))
    if not matching:
        return -1

    passwd = args["password"]
    if bcrypt.hashpw(passwd, matching[0].password) == matching[0].password:
        return matching[0].id

    return -1
