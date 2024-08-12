from pymongo import MongoClient

client = MongoClient('mongodb+srv://outfitradmin:Outfitrr@outfitr.3aqqnzz.mongodb.net/?retryWrites=true&w=majority&appName=outfitr')

db = client.outfitr_database
user_collection = db['user']
dataprofile_collection = db['user_dataprofiles']
products_collection = db['products']
user_activity_collection = db['user_activity']
todo_collection = db['todo_collection']
brand_collection = db['brands']
address_collection = db['addresses']
