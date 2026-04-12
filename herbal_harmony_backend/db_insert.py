from pymongo import MongoClient
import json

# MongoDB connect
client = MongoClient("mongodb://localhost:27017/")

# Database
db = client["herbal_ai"]

# Collection
collection = db["remedies"]

# collection.delete_many({})  # Clear existing data in the collection

# JSON file load
with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Insert data


if isinstance(data,list):
    collection.insert_many(data)
else:
    collection.insert_one(data)


print("✅ Fresh dataset inserted successfully!")

# print(db.list_collection_names())
# print(db["remedies"].count_documents({}))
# print(list(db["remedies"].find({"symptoms": ["headache"]})))