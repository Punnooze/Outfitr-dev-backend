from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')

client = MongoClient(MONGO_URI)

db = client.outfitr_database
user_collection = db['user']
dataprofile_collection = db['user_dataprofiles']
products_collection = db['products']
user_activity_collection = db['user_activity']
todo_collection = db['todo_collection']
brand_collection = db['brands']
address_collection = db['addresses']
order_collection = db['orders']
wishlist_collection = db['wishlist']
