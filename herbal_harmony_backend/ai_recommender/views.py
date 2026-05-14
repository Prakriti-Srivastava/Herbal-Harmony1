from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")
db = client["herbal_ai"]
collection = db["remedies"]

CATEGORY_RULES = {
    "cold": ["herbal", "yoga"],
    "cough": ["herbal", "yoga"],
    "fever": ["herbal"],
    "headache": ["herbal", "yoga", "mental"],
    "stress": ["mental", "yoga"],
    "anxiety": ["herbal", "mental", "yoga"],
    "sleep": ["mental"],
    "stomach pain": ["herbal", "yoga"],
    "fatigue": ["herbal", "yoga"],
    "digestion": ["herbal"],
    "back pain": ["yoga"],
    "joint pain": ["herbal","yoga"],
    "bee_sting": ["herbal", "yoga"]
}

AHP_WEIGHTS = {
    "symptom_match": 0.40,
    "effectiveness": 0.25,
    "safety": 0.15,
    "availability": 0.10,
    "severity": 0.10
}

def extract_symptoms(text):
    text = text.lower()

    synonyms = {
        "cold": [
            "cold", "runny nose", "blocked nose", "nose blocked"
            "sardi", "thand lag rahi", "naak band", "jukam", "zukam"
        ],

        "fever": [
            "fever","high temperature","temperature","feverish",
            "mild fever","viral fever","body temperature high",
            "burning body","hot body",

            "bukhar","tez bukhar","halka bukhar",
            "sharir garam","body garam lag rahi", "bukhar ho gaya", "bukhar ho gayi", "bukhar ho raha hai", "bukhar ho raha", "bukhar lag raha hai", "bukhar lag raha",
            "bukhar ho raha hai", "bukhar ho raha"
        ],

        "cough": [
            "cough","dry cough","wet cough","persistent cough",
        "throat cough","chest cough", 

        "khansi","khasi","sukhi khansi","balgam wali khansi",
        "gale ki khansi","seene ki khansi", "khansi ruk nahi rahi","khansi ruk nahi rahi hai", "khansi ho gayi", "khansi ho gaya"

        ],

        "headache": [
            "headache","head pain","heavy head","migraine",
            "forehead pain","head pressure", "head me pain","head me dard",

            "sar dard","sir dard","head me dard",
            "sar me pain","aadha sir dard", "puri sir dard", "sir dard ho gaya", "sir dard ho gayi", "sir dard ho raha hai", "sir dard ho raha"
        ],

        "stress": [
            "stress","tension","mental pressure","overthinking",
            "work stress","emotional stress", "mind stress", "stress ho raha hai", "stress ho raha",

            "tanav","pressure","bahut stress",
            "jyada sochna","dimag pe pressure", "kaam ka stress", "emotional stress", "tanav ho raha hai", "tanav ho raha"
        ],

        "anxiety": [
            "anxiety","nervous","panic","panic attack",
            "restlessness","fear","worried", 

            "ghabrahat","bechaini","dar lag raha", 
            "dil ghabra raha","anxious", "anxiety ho raha hai", "anxiety ho raha", "gabrahat ho rahi hai", "gabrahat ho rahi", "panic attack ho raha hai", "panic attack ho raha"
        ],

        "sleep": [
            "insomnia","poor sleep","cannot sleep",
            "sleep issue","sleep problem","sleeplessness",

            "neend nahi aa rahi",
            "neend nahi aati",
            "raat ko neend nahi aati", "raat ko neend nahi aati hai",
            "neend nahi aati", "neend nahi aati hai", 
        ],

        "stomach pain":[
            "stomach pain","abdomen pain","gas pain",
            "acidity","indigestion","bloating", 

            "pet dard","gas","pet me jalan",
            "badhazmi","pet phoolna", "pet me dard","pet me dard ho raha hai", "pet me dard ho raha" ,"pet dard ho gaya", "pet dard ho gayi"
        ],

        "fatigue":[
            "fatigue","tired","weakness","low energy",
            "body weakness",

            "thakan","kamzori","energy nahi",
            "bahut tired", "thakan ho rahi hai", "thakan ho rahi", "kamzori ho rahi hai", "kamzori ho rahi", "energy nahi hai", "energy nahi",
            "thakan ho gayi", "thakan ho gaya", "kamzori ho gayi", "kamzori ho gaya", "energy nahi hai", "energy nahi"
        ],

        "digestion":[
            "digestive issue","constipation","loose motion",
            "diarrhea","indigestion",

            "kabz","pet kharab","dast",
            "pachan problem", "pachan me problem", "pachan me dikkat", "pachan me dikkat ho rahi hai", "pachan me dikkat ho rahi", "dast ho gaya", "dast ho gayi"
         
        ],

        "back pain":[
            "back pain","lower back pain","spine pain",

            "kamar dard","peeth dard", "lower back dard","spine dard", "kamar me dard", "peeth me dard", "kamar me dard ho raha hai", "peeth me dard ho raha hai" , "kamar me dard ho raha", "peeth me dard ho raha", "lower back dard ho raha hai", "lower back dard ho raha"
        ],


        "joint pain":[
            "joint pain","knee pain","arthritis pain",

            "ghutne dard","jodo me dard", "joint me dard", "joint me dard ho raha hai", "joint me dard ho raha", "ghutne me dard", "ghutne me dard ho raha hai", "ghutne me dard ho raha", "arthritis me dard", "arthritis me dard ho raha hai", "arthritis me dard ho raha" , "arthritis dard", "arthritis dard ho gaya", "arthritis dard ho gayi"
        ],

        "bee_sting": [
            "bee sting","honey bee sting","bee bite",
            "bee attack","insect sting",

            "madhumakhi kaat li","madhumakhi ne kaata","bee ne kaata", "bee ne kaat liya", "bee ne kaata hai", "keede ne kaata", "keede ne kaat liya", "keede ne kaata hai", "dank laga","dank mara" , "madhumakhi kaat liya", "madhumakhi ne kaata hai", "bee ne kaata hai", "keede ne kaata hai", "dank laga","dank mara" , "madhumakhi kaat liya", "madhumakhi ne kaata hai", "bee ne kaata hai", "keede ne kaata hai", "dank laga","dank mara" , "madhumakhi kaat liya", "madhumakhi ne kaata hai", "bee ne kaata hai", "keede ne kaata hai", "dank laga","dank mara" , "madhumakhi kaat liya", "madhumakhi ne kaata hai", "bee ne kaata hai", "keede ne kaata hai", "dank laga","dank mara" , "madhumakhi kaat liya", "madhumakhi ne kaata hai", "bee ne kaata hai", "keede ne kaata hai", "dank laga","dank mara" , "madhumakhi kaat liya", "madhumakhi ne kaata hai", "bee ne kaata hai", "keede ne kaata hai", "dank laga","dank mara" , "madhumakhi kaat liya", "madhumakhi ne kaata hai", "bee ne kaata hai", "keede ne kaata hai", "dank laga","dank mara" , "madhumakhi kaat liya", "madhumakhi ne kaata hai", "bee ne kaata hai", "keede ne kaata hai", "dank laga","dank mara" , "madhumakhi kaat liya", "madhumakhi ne kaata hai", "bee ne kaata hai",
            "keede ne kaata","dank laga","dank mara" , "madhumakhi kaat liya", "madhumakhi ne kaata hai", "bee ne kaata hai", "keede ne kaata hai", "dank laga hai", "dank mara hai"
        ],

        # "sting_reaction":[
        #     "swelling","pain","burning","redness","itching",

        #     "sujan","jalan","dard","lal ho gaya","khujli" 
        # ],


    }

    found = []

    for symptom, words in synonyms.items():
        for word in words:
            if word in text:
                found.append(symptom)

    return list(set(found))

def get_required_types(symptoms):
    required = set()
    for symptom in symptoms:
        if symptom in CATEGORY_RULES:
            required.update(CATEGORY_RULES[symptom])
    return list(required)

def calculate_match(user_symptoms, item_symptoms):
    user_set = set(user_symptoms)
    item_set = set(item_symptoms)

    common = user_set.intersection(item_set)
    match_count = len(common)
    match_ratio = match_count / len(user_set) if user_set else 0

    exact_match = user_set == item_set
    subset_match = user_set.issubset(item_set)

    return match_count, match_ratio, exact_match, subset_match

def calculate_ahp_score(item, user_symptoms):
    item_symptoms = item.get("symptoms", [])

    match_count, match_ratio, exact_match, subset_match = calculate_match(
        user_symptoms, item_symptoms
    )

    symptom_match_score = match_ratio * 10
    effectiveness = item.get("effectiveness", 5)
    safety = item.get("safety", 5)
    availability = item.get("availability", 5)
    severity = item.get("severity", 5)

    score = (
        symptom_match_score * AHP_WEIGHTS["symptom_match"] +
        effectiveness * AHP_WEIGHTS["effectiveness"] +
        safety * AHP_WEIGHTS["safety"] +
        availability * AHP_WEIGHTS["availability"] +
        severity * AHP_WEIGHTS["severity"]
    )

    if exact_match:
        score += 2.0
    elif subset_match:
        score += 1.0

    return round(score, 2), match_count, match_ratio, exact_match, subset_match

@csrf_exempt
def recommend(request):
    if request.method == "GET":
        return JsonResponse({"message": "Use POST request with symptoms"})

    if request.method != "POST":
        return JsonResponse({"error": "Only POST method allowed"}, status=405)

    try:
        data = json.loads(request.body)
        user_input = data.get("symptoms", "").strip()

        if not user_input:
            return JsonResponse({"error": "Symptoms are required"}, status=400)

        user_symptoms = extract_symptoms(user_input)

        if not user_symptoms:
            return JsonResponse({
                "input_text": user_input,
                "detected_symptoms": [],
                "show_herbal": False,
                "show_yoga": False,
                "show_mental": False,
                "herbal": [],
                "yoga": [],
                "mental": [],
                "message": "No known symptoms detected."
            })

        required_types = get_required_types(user_symptoms)
        items = list(collection.find({"type": {"$in": required_types}}))

        scored_items = []
        for item in items:
            item.pop("_id", None)

            score, match_count, match_ratio, exact_match, subset_match = calculate_ahp_score(
                item, user_symptoms
            )

            if match_count > 0:
                item["score"] = score
                item["match_count"] = match_count
                item["match_ratio"] = round(match_ratio, 2)
                item["exact_match"] = exact_match
                item["subset_match"] = subset_match
                scored_items.append(item)

        scored_items.sort(
            key=lambda x: (
                x["exact_match"],
                x["match_count"],
                x["score"]
            ),
            reverse=True
        )

        herbal = []
        yoga = []
        mental = []

        used_names = set()

        for item in scored_items:
            item_name = item.get("name", "").strip().lower()

            if item_name in used_names:
                continue

            cleaned = {
                "name": item.get("name"),
                "description": item.get("description") or "No description available.",
                "link": item.get("link"),
                "score": item.get("score")
            }

            if item["type"] == "herbal" and len(herbal) < 2:
                herbal.append(cleaned)
                used_names.add(item_name)

            elif item["type"] == "yoga" and len(yoga) < 2:
                yoga.append(cleaned)
                used_names.add(item_name)

            elif item["type"] == "mental" and len(mental) < 2:
                mental.append(cleaned)
                used_names.add(item_name)


        return JsonResponse({
            "input_text": user_input,
            "detected_symptoms": user_symptoms,
            "show_herbal": len(herbal) > 0,
            "show_yoga": len(yoga) > 0,
            "show_mental": len(mental) > 0,
            "herbal": herbal,
            "yoga": yoga,
            "mental": mental
        }, safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    
    return JsonResponse({"error": "Only POST method allowed"}, status=405)








# from pymongo import MongoClient
# import json
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt


# # MongoDB connect
# client = MongoClient("mongodb://localhost:27017/")
# db = client["herbal_ai"]
# collection = db["remedies"]

# # OpenAI setup


# # AI: extract symptoms
# # def extract_symptoms(text):
# #     prompt = f"""
# #     Extract symptoms from this text:
# #     {text}
# #     Return list like ["cold","fever"]
# #     """

# #     response = client_ai.responses.create(
# #         model="gpt-4.1-mini",
# #         input=prompt
# #     )

# #     return eval(response.output[0].content[0].text)

# def extract_symptoms(text):
#     text = text.lower()

#     synonyms = {
#         "cold": ["cold", "runny nose", "blocked nose"],
#         "fever": ["fever", "high temperature", "feverish"],
#         "cough": ["cough", "dry cough"],
#         "stress": ["stress", "tension"],
#         "anxiety": ["anxiety", "nervous"]
#     }

#     found = []

#     for key, words in synonyms.items():
#         for w in words:
#             if w in text:
#                 found.append(key)

#     return list(set(found))


# # Match score
# def match_score(user, item):
#     return len(set(user) & set(item))

# # AHP score
# def calculate_score(item, user):
#     match = match_score(user, item["symptoms"])

#     return (
#         item.get("effectiveness",5)*0.4 +
#         item.get("safety",5)*0.2 +
#         item.get("availability",5)*0.1 +
#         match*0.3
#     )




# # MAIN API
# # def recommend(request):
# #     if request.method == "POST":
# #         data = json.loads(request.body)

# #         user_input = data["symptoms"]

# #         # AI se symptoms nikalo
# #         user_symptoms = extract_symptoms(user_input)

# #         items = list(collection.find())

# #         for item in items:
# #             item["score"] = calculate_score(item, user_symptoms)

# #         sorted_items = sorted(items, key=lambda x: x["score"], reverse=True)

# #         return JsonResponse(sorted_items[:5], safe=False)
    
# # def test_openai(request):
# #     response = client_ai.responses.create(
# #         model="gpt-4.1-mini",
# #         input="Say hello"
# #     )

# #     return JsonResponse({
# #         "result": response.output[0].content[0].text
# #     })


# @csrf_exempt
# def recommend(request):
#     # ✅ IMPORTANT: handle GET request
#     if request.method == "GET":
#         return JsonResponse({"message": "Use POST request with symptoms"})
    
#     if request.method != "POST":
#         return JsonResponse({"error": "Only POST allowed"}, status=405)

#     try:
#         data = json.loads(request.body)
#         user_input = data.get("symptoms", "")
#         user_symptoms = extract_symptoms(user_input)

#         remedies = list(db.herbal_remedies.find())

#         def match_score(user_symptoms, item_symptoms):
#             return len(set(user_symptoms) & set(item_symptoms))

#         def calculate_score(item):
#             match = match_score(user_symptoms, item["symptoms"])
#             return (
#                 item["effectiveness"] * 0.4 +
#                 item["safety"] * 0.2 +
#                 item["availability"] * 0.1 +
#                 match * 0.3
#             )

#         for r in remedies:
#             r["score"] = calculate_score(r)

#         sorted_results = sorted(remedies, key=lambda x: x["score"], reverse=True)

#         # remove _id (MongoDB problem fix)
#         for r in sorted_results:
#             r.pop("_id", None)

#         return JsonResponse(sorted_results[:5], safe=False)

#     except Exception as e:
#         return JsonResponse({"error": str(e)})
    
#     #     items = list(collection.find())
#     #     debug_items = []
#     #     for item in items:
#     #         item.pop("_id", None)
#     #         if "symptoms" in item:
#     #             item["score"] = calculate_score(item, user_symptoms)
#     #         else:
#     #             item["score"] = 0
#     #         debug_items.append(item)
#     #     sorted_items = sorted(debug_items, key=lambda x: x["score"], reverse=True)

#     #     return JsonResponse({
#     #         "input": user_input,
#     #         "detected_symptoms": user_symptoms,
#     #         "total_items_in_db": len(debug_items),
#     #         "top_results": sorted_items[:5]
#     #     }, safe=False)
    
#     # except Exception as e:
#     #     return JsonResponse({"error": str(e)}, status=500)

# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from pymongo import MongoClient
# import json

# # 🔗 MongoDB Connection (Ensure same as db_insert.py)
# client = MongoClient("mongodb://localhost:27017/")
# db = client["herbal_ai"]          # Database name
# collection = db["remedies"]       # Collection name

# # 🧠 Simple NLP function to extract symptoms
# def extract_symptoms(text):
#     text = text.lower()

#     synonyms = {
#         "cold": ["cold", "runny nose", "blocked nose"],
#         "fever": ["fever", "high temperature", "feverish"],
#         "cough": ["cough", "dry cough"],
#         "stress": ["stress", "tension"],
#         "anxiety": ["anxiety", "nervous"]
#     }

#     found = []
#     for key, words in synonyms.items():
#         for word in words:
#             if word in text:
#                 found.append(key)

#     return list(set(found))

# # 🔢 AHP-based scoring
# def match_score(user_symptoms, item_symptoms):
#     return len(set(user_symptoms) & set(item_symptoms))

# def calculate_score(item, user_symptoms):
#     match = match_score(user_symptoms, item.get("symptoms", []))
#     return (
#         item.get("effectiveness", 5) * 0.4 +
#         item.get("safety", 5) * 0.2 +
#         item.get("availability", 5) * 0.1 +
#         match * 0.3
#     )

# # 🚀 Main Recommendation API
# @csrf_exempt
# def recommend(request):
#     # Handle GET request (for browser testing)
#     if request.method == "GET":
#         return JsonResponse({
#             "message": "API is working. Please send a POST request with symptoms."
#         })

#     # Handle POST request
#     if request.method == "POST":
#         try:
#             # Parse user input
#             data = json.loads(request.body)
#             user_input = data.get("symptoms", "")

#             # Extract symptoms using NLP
#             user_symptoms = extract_symptoms(user_input)

#             # Fetch all items from MongoDB
#             items = list(collection.find())

#             # Prepare results with scoring
#             results = []
#             for item in items:
#                 item.pop("_id", None)  # Remove MongoDB ObjectId
#                 item["score"] = calculate_score(item, user_symptoms)
#                 results.append(item)

#             # Sort by score (highest first)
#             sorted_results = sorted(results, key=lambda x: x["score"], reverse=True)

#             # Debug response to understand what's happening
#             return JsonResponse({
#                 "input_text": user_input,
#                 "detected_symptoms": user_symptoms,
#                 "total_items_in_database": len(results),
#                 "top_recommendations": sorted_results[:5]
#             }, safe=False)

#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)

#     # If method is not allowed
#     return JsonResponse({"error": "Only POST method allowed"}, status=405)



   