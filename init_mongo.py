from pymongo import MongoClient

client = MongoClient("mongodb://mongo_perpus:27017")  
db = client["perpustakaan"]
reviews = db["reviews"]

reviews.insert_one({
    "book_id": 1,
    "reviews": [
        {
            "user_id": 10223001,
            "username": "Andi Saputra",
            "rating": 4.5,
            "comment": "Sangat membantu untuk skripsian saya.",
            "date": "2025-06-27"
        }
    ]
})
