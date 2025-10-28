from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['herbal_harmony']
herbs = db['herbs']

result = herbs.find_one({
    "Symptom": "cold",
    "age_group": "child"
})

print("Result:", result)

