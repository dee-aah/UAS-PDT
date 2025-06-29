-- Tabel buku
CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  author VARCHAR(255),
  published_year INT,
  isbn VARCHAR(20) UNIQUE
);

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  nim INT,
  email VARCHAR(255) UNIQUE
);

CREATE TABLE availability (
  book_id INT PRIMARY KEY REFERENCES books(id),
  total_copies INT NOT NULL,
  available_copies INT NOT NULL
);

CREATE TABLE loans (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    book_id INT REFERENCES books(id),
    loan_date DATE NOT NULL DEFAULT CURRENT_DATE,
    due_date DATE NOT NULL,
    status VARCHAR(20) DEFAULT 'dipinjam', -- dipinjam, terlambat, diperpanjang
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE loan_history (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    book_id INT REFERENCES books(id),
    loan_date DATE NOT NULL,
    return_date DATE,
    status VARCHAR(20),  
    duration INTEGER,     
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


docker exec -it postgres_perpus psql -U user -d perpus_db
SELECT * FROM books;

-- Tambahkan data buku
INSERT INTO books (title, author, published_year, isbn) VALUES
('Basis Data Terdistribusi', 'Dr. Bambang', 2022, '9786021234567'),
('Struktur Data', 'Ir. Siti Aminah', 2021, '9786029876543'),
('Algoritma Pemrograman', 'Rudi Hartono', 2023, '9786021122334');

INSERT INTO users (name, nim, email) VALUES
('Andi Saputra', 10223001, 'andi@sttcipasung.ac.id'),
('Siti Rahmawati', 10223002, 'siti@sttcipasung.ac.id'),
('Budi Nugraha', 10223003, 'budi@sttcipasung.ac.id');

INSERT INTO availability (book_id, total_copies, available_copies) VALUES
(1, 5, 3),
(2, 4, 2),
(3, 3, 0);

INSERT INTO loans (user_id, book_id, loan_date, due_date, status)
VALUES
(1, 1, '2025-06-25', '2025-07-05', 'dipinjam'),
(2, 2, '2025-06-26', '2025-07-06', 'dipinjam'),
(3, 3, '2025-06-27', '2025-07-07', 'dipinjam');

INSERT INTO loan_history (user_id, book_id, loan_date, return_date, status, duration)
VALUES
(1, 1, '2025-06-10', '2025-06-20', 'dikembalikan', 10),
(2, 2, '2025-06-01', '2025-06-15', 'dikembalikan', 14),
(3, 3, '2025-05-15', '2025-06-01', 'hilang', 17);

--untuk mongodb
docker exec -it mongo_perpus mongosh
use perpustakaan 
db.reviews.find()
--untuk redis
docker exec -it redis_perpus redis-cli
KEYS *
-- insert lewat python untuk redis dan mongo
docker exec -it python_app python init_redis_mongo.py

docker exec -it pg_coordinator psql -U postgres
SELECT * FROM master_add_node('pg_worker', 5432);

CREATE TABLE reviews (
  book_id INT,
  user_id INT,
  comment TEXT,
  rating NUMERIC
);

SELECT create_distributed_table('reviews', 'book_id');

INSERT INTO reviews VALUES
 (1, 1, 'Sangat menarik', 4.5),
 (2, 2, 'Lumayan', 3.8),
 (3, 3, 'Kurang detail', 3.0);

SELECT * FROM pg_dist_placement;

docker exec -it pg_worker_replica psql -U postgres
