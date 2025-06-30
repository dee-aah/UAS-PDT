import psycopg2
import redis
from pymongo import MongoClient
from pprint import pprint

# PostgreSQL
pg_conn = psycopg2.connect(
    dbname="perpus_db",
    user="user",
    password="pass",
    host="postgres_perpus",
    port=5432
)
pg_cursor = pg_conn.cursor()

# Redis
r = redis.Redis(host='redis_perpus', port=6379, decode_responses=True)

# MongoDB
mongo = MongoClient("mongodb://mongo_perpus:27017")
reviews_collection = mongo["perpustakaan"]["reviews"]

pg_cursor.execute("""
    SELECT br.id, br.book_id, br.user_id, br.loan_date,
           u.name AS name, u.email,
           b.title, b.author
    FROM loan_history br
    JOIN users u ON br.user_id = u.id
    JOIN books b ON br.book_id = b.id;
""")

rows = pg_cursor.fetchall()

# --- Gabungkan dengan ulasan dari MongoDB
for row in rows:
    user_id, book_id, user_id, loan_date, name, email, title, author = row
    review_doc = reviews_collection.find_one({"book_id": book_id})
    reviews = review_doc["reviews"] if review_doc else []

    print(f"Peminjaman #{user_id}")
    print(f"- Buku    : {title} oleh {author}")
    print(f"- Peminjam: {name} ({email})")
    print(f"- Tanggal : {loan_date}")
    print(f"- Ulasan  :")

    if reviews:
        for rev in reviews:
            print(f"  • {rev['username']} ({rev['rating']}) - {rev['comment']}")
    else:
        print("  • Belum ada ulasan.")
    print("-" * 40)

pg_cursor.close()
pg_conn.close()