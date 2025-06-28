-- Tabel buku
CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  author VARCHAR(255),
  published_year INT,
  isbn VARCHAR(20) UNIQUE
);

-- Tabel pengguna
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  nim INT,
  email VARCHAR(255) UNIQUE
);

-- Tabel ketersediaan buku
CREATE TABLE availability (
  book_id INT PRIMARY KEY REFERENCES books(id),
  total_copies INT NOT NULL,
  available_copies INT NOT NULL
);

-- Tabel peminjaman buku 
CREATE TABLE loan_history (
  id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(id),
  book_id INT REFERENCES books(id),
  loan_date DATE NOT NULL,
  return_date DATE,
  status VARCHAR(20) DEFAULT 'dipinjam' 
);

-- Tambahkan data buku
INSERT INTO books (title, author, published_year, isbn) VALUES
('Basis Data Terdistribusi', 'Dr. Bambang', 2022, '9786021234567'),
('Struktur Data', 'Ir. Siti Aminah', 2021, '9786029876543'),
('Algoritma Pemrograman', 'Rudi Hartono', 2023, '9786021122334');

-- Tambahkan data pengguna
INSERT INTO users (name, nim, email) VALUES
('Andi Saputra', 10223001, 'andi@sttcipasung.ac.id'),
('Siti Rahmawati', 10223002, 'siti@sttcipasung.ac.id'),
('Budi Nugraha', 10223003, 'budi@sttcipasung.ac.id');

-- Tambahkan data ketersediaan buku
INSERT INTO availability (book_id, total_copies, available_copies) VALUES
(1, 5, 3),
(2, 4, 2),
(3, 3, 0);

-- Tambahkan data riwayat peminjaman
INSERT INTO loan_history (user_id, book_id, loan_date, return_date, status) VALUES
(1, 1, '2025-06-20', NULL, 'dipinjam'),
(2, 2, '2025-06-18', '2025-06-25', 'dikembalikan'),
(3, 3, '2025-06-15', NULL, 'terlambat');

