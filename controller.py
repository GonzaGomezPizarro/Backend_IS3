from database import mongo
from models import User

def GetUsers():
    return mongo.get_users()

def GetUserByUsername(username):
    return mongo.get_user(username)

def InsertUser(user: User):
    user = mongo.insert_user(user.dict())
