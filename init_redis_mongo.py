import redis
from pymongo import MongoClient

# --- Redis ---
r = redis.Redis(host='redis_perpus', port=6379, decode_responses=True)

r.set("book:1:available", 3)
r.set("book:2:available", 2)
r.set("book:3:available", 0)
print("✅ Redis siap.")

# --- MongoDB ---
mongo = MongoClient("mongodb://mongo_perpus:27017")
db = mongo["perpustakaan"]
reviews = db["reviews"]

reviews.delete_many({})  # Kosongkan dulu
reviews.insert_one({
    "book_id": 1,
    "reviews": [
        {
            "user_id": 1,
            "username": "Andi",
            "rating": 4.5,
            "comment": "Bagus banget buat TA",
            "date": "2025-06-28"
        }
    ]
})
print("✅ MongoDB siap.")
