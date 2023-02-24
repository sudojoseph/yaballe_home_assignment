import pymongo
import os


MONGO_PASSWORD = os.getenv('MONGO_DB_PASSWORD_YABALLE')


client = pymongo.MongoClient(f"mongodb+srv://yaballe:{MONGO_PASSWORD}@yaballe.wcwm7yz.mongodb.net/?retryWrites=true&w=majority")
db = client.db
products_collection = db['products']
user_collection = db['users']