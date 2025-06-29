import redis
from pymongo import MongoClient

# --- Redis ---
r = redis.Redis(host='redis_perpus', port=6379, decode_responses=True)

r.set("book:1:available", 3)
r.set("book:2:available", 2)
r.set("book:3:available", 0)
print(" Redis siap.")

# --- MongoDB ---
mongo = MongoClient("mongodb://mongo_perpus:27017")
db = mongo["perpustakaan"]
reviews = db["reviews"]

reviews.insert_one({
    "book_id": 1,
    "reviews": [
        {
            "user_id": 1,
            "username": "Eko",
            "rating": 4.8,
            "comment": "Sangat berguna untuk kuliah DBD.",
            "date": "2025-06-29"
        },
        {
            "user_id": 2,
            "username": "Dina",
            "rating": 3.5,
            "comment": "Lumayan, tapi terlalu teknis.",
            "date": "2025-06-29"
        },
        {
            "user_id": 3,
            "username": "Ali",
            "rating": 4.0,
            "comment": "Bahasannya cukup lengkap dan mudah dipahami.",
            "date": "2025-06-29"
        }
    ]
})

print(" MongoDB siap.")
