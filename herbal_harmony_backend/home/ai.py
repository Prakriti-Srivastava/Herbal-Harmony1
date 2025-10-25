from pymongo import MongoClient

# Step 1 – MongoDB connection
client = MongoClient("mongodb://localhost:27017/")  # localhost par mongo run hota hai
db = client['herbal_harmony']  # database ka naam
herbs_collection = db['herbs']
yoga_collection = db['yoga']

def getRemedyAndYoga(age_group, symptom):
    # Step 2 – Remedy find karo
    remedy = herbs_collection.find_one({
        "Symptom": symptom,
        "age_group": age_group
    })

    # Step 3 – Yoga find karo
    yoga = yoga_collection.find_one({
        "Symptom": symptom,
        "age_group": age_group
    })

    # Step 4 – Output return karo
    if remedy and yoga:
        return {
            "remedy": remedy['remedy'],
            "link_remedy": remedy['link'],
            "yoga": yoga['yoga'],
            "link_yoga": yoga['link']
        }
    else:
        return None

    

    # # symptom ko lowercase me le lo (user uppercase bhi likh sakta hai)
    # symptom = symptom.lower()

    # # ab logic lagao
    # if age_group in remedies and symptom in remedies[age_group]:
    #     return remedies[age_group][symptom]
    # else:
    #     return None



























































# # ai.py
# from pymongo import MongoClient

# # Step 1: Connect to MongoDB (local server)
# client = MongoClient("mongodb://localhost:27017/")

# # Step 2: Create a new database (if not exist, it will be created)
# db = client["herbal_harmony2"]

# # Step 3: Create collections
# herbs_collection = db["herbs2"]
# yoga_collection = db["yoga2"]

# # Step 4: Insert sample data (herbs)
# herb_docs = [
#     {
#         "ailment": "cold",
#         "age_group": "child",
#         "remedy": "Tulsi Honey Mix",
#         "link": "Home.html",
#         "notes": "1 tsp honey with 2-3 crushed tulsi leaves; safe for kids above 5."
#     },
#     {
#         "ailment": "cold",
#         "age_group": "adult",
#         "remedy": "Tulsi Tea",
#         "link": "/herbal-remedies/tulsi",
#         "notes": "Boil 6-7 tulsi leaves in 1 cup water; drink warm twice a day."
#     },
#     {
#         "ailment": "fatigue",
#         "age_group": "elderly",
#         "remedy": "Ginger Tea with Honey",
#         "link": "/herbal-remedies/ginger",
#         "notes": "Mild energy booster for elderly."
#     }
# ]

# herbs_collection.insert_many(herb_docs)

# # Step 5: Insert sample data (yoga)
# yoga_docs = [
#     {
#         "benefit": "cold",
#         "age_group": "child",
#         "yoga": "Balasana (Child Pose)",
#         "link": "/yoga/child-pose",
#         "instructions": "Hold for 20 sec, repeat 3 times."
#     },
#     {
#         "benefit": "cold",
#         "age_group": "adult",
#         "yoga": "Surya Namaskar",
#         "link": "/yoga/surya-namaskar",
#         "instructions": "5 rounds every morning."
#     },
#     {
#         "benefit": "fatigue",
#         "age_group": "elderly",
#         "yoga": "Anulom Vilom",
#         "link": "/yoga/anulom-vilom",
#         "instructions": "5 mins daily; improves breathing."
#     }
# ]

# yoga_collection.insert_many(yoga_docs)

# # Step 6: Query data to verify
# print("\n✅😄 All herbs in database:")
# for herb in herbs_collection.find():
#     print(herb)

# print("\n✅😄 All yoga poses in database:")
# for yoga in yoga_collection.find():
#     print(yoga)





# import pymongo

# if __name__ == "__main__":
    
#     print("Hello, Herbal harmony !")
#     myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#     (myclient)

# mydb = myclient["mydatabase"]




# remedies = {
#     "headache": [
#         "Peppermint tea",
#         "Ginger tea",
#         "Lavender essential oil",
#         "Willow bark",
#         "Chamomile tea"
#     ],
#     "cold": [
#         "Echinacea tea",
#         "Honey and lemon",
#         "Ginger tea",
#         "Garlic",
#         "Peppermint tea"
#     ],
#     "anxiety": [
#         "Chamomile tea",
#         "Lavender essential oil",
#         "Valerian root",
#         "Lemon balm tea",
#         "Passionflower"
#     ],
#     "insomnia": [
#         "Chamomile tea",
#         "Valerian root",
#         "Lavender essential oil",
#         "Passionflower tea",
#         "Magnesium supplements"
#     ],
#     "digestive issues": [
#         "Ginger tea",
#         "Peppermint tea",
#         "Fennel seeds",
#         "Chamomile tea",
#         "Slippery elm"
#     ]
# }

# symptom = input("Enter your symptom (headache, cold, anxiety, insomnia, digestive issues): ").strip().lower()
# print("Suggested remedy : ", remedies.get(symptom, "Sorry, no remedy found for that symptom."))


# remedies = {
#         'child': {
#             'cold': {
#                 'remedy': 'Tulsi Honey Mix',
#                 'yoga': 'Balasana (Child Pose)',
#                 'link_remedy': '/tulsi',
#                 'link_yoga': '/kapalbhati'
#             },
#             'fever': {
#                 'remedy': 'Ginger Honey Tea',
#                 'yoga': 'Anulom Vilom',
#                 'link_remedy': '/herbal-remedies/ginger-honey',
#                 'link_yoga': '/yoga/anulom-vilom'
#             }
#         },
#         'adult': {
#             'stress': {
#                 'remedy': 'Ashwagandha Tea',
#                 'yoga': 'Surya Namaskar',
#                 'link_remedy': '/herbal-remedies/ashwagandha-tea',
#                 'link_yoga': '/yoga/surya-namaskar'
#             },
#             'headache': {
#                 'remedy': 'Peppermint Tea',
#                 'yoga': 'Anulom Vilom',
#                 'link_remedy': '/herbal-remedies/peppermint-tea',
#                 'link_yoga': '/yoga/anulom-vilom'
#             }
#         },
#         'elderly': {
#             'joint pain': {
#                 'remedy': 'Turmeric Milk',
#                 'yoga': 'Tadasana',
#                 'link_remedy': '/herbal-remedies/turmeric-milk',
#                 'link_yoga': '/yoga/tadasana'
#             },
#             'weakness': {
#                 'remedy': 'Amla Juice',
#                 'yoga': 'Pranayama',
#                 'link_remedy': '/herbal-remedies/amla-juice',
#                 'link_yoga': '/yoga/pranayama'
#             }
#         }
#     }