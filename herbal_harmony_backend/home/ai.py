from pymongo import MongoClient


# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client['herbal_harmony']
herbscol = db['herbs']
yogacol = db['yoga']

# Free text keyword mapping
symptomkeywords = {
    "cold": ["cold", "jhukham", "sardi", "thand lag rahi hai", "mujhe jhukham hai", "nasa band hai"],
    "headache": ["sir dard", "headache", "sir me dard ho raha hai", "dard sir ka"],
    "fever": ["bukhaar", "fever", "bukhar", "body temperature badh gaya"],
    "stress": ["stress", "tanaav", "mujhe stress hai", "dimag par bojh hai", "mera dimag khrab ho rha hai"],
    "joint pain": ["joint pain", "jodon ka dard", "gathiya", "mere jodon me dard hai", "haddi dard"],
    "fatigue": ["thakan", "fatigue", "bahut thak gaya hoon", "energy kam hai", "kamzori mehsoos ho rhi hai"],
    "anxiety": ["chinta", "anxiety", "mujhe chinta ho rhi hai", "nervousness", "bechaini"],
    "insomnia": ["neend na aana", "insomnia", "sone me dikkat", "neend nahi aati", "sleep problems"],
    "digestive issues": ["pachak samasya", "digestive issues", "pet ki problem", "indigestion", "pet dard", "khana hazam nahi hota"],
    "vomiting": ["ulti", "vomiting", "mujhe ulti ho rhi hai", "pet kharab hai", "nausea"],
    "body pain": ["body pain", "dard ho raha hai", "pure sharir me dard hai", "sarir dard", "sari body me pain hai", "sharir me jalan hai", "thakan aur dard", "muscle pain", "sharir dard kar raha hai"]

}

def getRemedyAndYoga(age_group, symptom):
    # Normalize inputs
    age_group = age_group.strip().lower()
    symptom = symptom.strip().lower()

    # Map free text input to symptom keyword
    symptomkey = None
    for key, phrases in symptomkeywords.items():
        for phrase in phrases:
            if phrase in symptom:
                symptomkey = key
                break
        if symptomkey:
            break

    if not symptomkey:
        print("No matching symptom keyword found:", symptom)
        return None

    print(" User Input:", symptom, "Mapped Symptom:", symptomkey)

    # Query MongoDB using mapped keyword
    remedy = herbscol.find_one({
        "Symptom": {"$regex": f"^{symptomkey}$", "$options": "i"},
        "age_group": {"$regex": f"^{age_group}$", "$options": "i"}
    })


    yoga = yogacol.find_one({
        "Symptom": {"$regex": f"^{symptomkey}$", "$options": "i"},
        "age_group": {"$regex": f"^{age_group}$", "$options": "i"}
    })

    print("Remedy found:", remedy)
    print("Yoga found:", yoga)
    # Return results

    if remedy or yoga:
        return {
            "remedy": remedy['remedy'] if remedy else "No remedy found",
            "link_remedy": remedy['link'] if remedy else "#",
            "yoga": yoga['yoga'] if yoga else "No yoga found",
            "link_yoga": yoga['link'] if yoga else "#"
        }
    else:
        return None
# # ai.py




























































































































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