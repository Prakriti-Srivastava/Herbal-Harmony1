from pymongo import MongoClient
import json
from pathlib import Path 

# MongoDB connect
client = MongoClient("mongodb://localhost:27017/")

# Database
db = client["herbal_ai"]

# Collection
collection = db["remedies"]

BASE_DIR = Path(__file__).resolve().parent
json_path = BASE_DIR / "data.json"

# JSON file load
with open(json_path, "r", encoding="utf-8") as file:
    data = json.load(file)

collection.delete_many({})  # Clear existing data in the collection

# Insert data
collection.insert_many(data)

print("✅ Fresh dataset inserted successfully!")

# print(db.list_collection_names())
# print(db["remedies"].count_documents({}))
# print(list(db["remedies"].find({"symptoms": ["headache"]})))