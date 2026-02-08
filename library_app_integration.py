import psycopg2
import redis
from pymongo import MongoClient
from pprint import pprint

# --- KONEKSI POSTGRESQL ---
pg_conn = psycopg2.connect(
    dbname="perpus_db",
    user="user",
    password="pass",
    host="postgres_perpus",
    port=5432
)

r = redis.Redis(host='redis_perpus', port=6379, decode_responses=True)

# --- KONEKSI MONGODB ---
mongo_client = MongoClient("mongodb://mongo_perpus:27017,mongo_perpus_secondary:27017/?replicaSet=rs0")
mongo_db = mongo_client["perpustakaan"]
reviews_collection = mongo_db["reviews"]
pg_cursor = pg_conn.cursor() 
def get_book_detail(book_id):
    # Ambil data buku dari PostgreSQL
    pg_cursor.execute("""
        SELECT b.id, b.title, b.author, a.available_copies
        FROM books b
        JOIN availability a ON b.id = a.book_id
        WHERE b.id = %s
    """, (book_id,))
    book = pg_cursor.fetchone()

    if not book:
        return "Buku tidak ditemukan."

    # Ambil ketersediaan dari Redis
    redis_available = r.get(f"book:{book_id}:available")

    # Ambil ulasan dari MongoDB
    review_doc = reviews_collection.find_one({"book_id": book_id})
    reviews = review_doc["reviews"] if review_doc else []

    return {
        "id": book[0],
        "title": book[1],
        "author": book[2],
        "available_pg": book[3],
        "available_redis": redis_available,
        "reviews": reviews
    }

if __name__ == "__main__":
    book_id = 1  # Ganti dengan ID buku sesuai database
    detail = get_book_detail(book_id)
    pprint(detail)

    pg_cursor.close()
    pg_conn.close()
