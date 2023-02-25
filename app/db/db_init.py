import pymongo
import os


MONGO_PASSWORD = os.getenv('MONGO_DB_PASSWORD_YABALLE')

try:
    client = pymongo.MongoClient(f"mongodb+srv://yaballe:{MONGO_PASSWORD}@yaballe.wcwm7yz.mongodb.net/?retryWrites=true&w=majority")
    db = client.db
    products_collection = db['products']
    user_collection = db['users']
except TypeError:
    print('MongoDB password not set correctly, please add it to your system by "export MONGO_DB_PASSWORD_YABALLE=<password>"')
except pymongo.errors.ConnectionFailure:
    print('Not able to connect to MongoDB')
except pymongo.errors.AutoReconnect:
    print('Lost connection to MongoDB')