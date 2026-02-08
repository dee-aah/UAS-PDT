import redis
from pymongo import MongoClient
from pymongo.errors import PyMongoError

# --- Redis ---
try:
    r = redis.Redis(host='redis_perpus', port=6379, decode_responses=True)
    r.ping()
    r.set("book:1:available", 3)
    r.set("book:2:available", 2)
    r.set("book:3:available", 0)
    print("Redis siap.")
except Exception as e:
    print("Redis error:", e)

# --- MongoDB ---
try:
    mongo = MongoClient("mongodb://mongo_perpus:27017,mongo_perpus_secondary:27017/?replicaSet=rs0")
    mongo.admin.command("ping")  # tes koneksi ke PRIMARY
    db = mongo["perpustakaan"]
    reviews = db["reviews"]

    result = reviews.insert_one({
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

    print("MongoDB siap. Inserted ID:", result.inserted_id)

except PyMongoError as e:
    print("MongoDB insert error:", e)
except Exception as e:
    print("MongoDB general error:", e)
