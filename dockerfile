# Gunakan image Python yang ringan
FROM python:3.10-slim

# Direktori kerja di dalam container
WORKDIR /app

# Salin requirements dan install dependency
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua file aplikasi ke dalam container
COPY . .

# Jalankan program Python utama
CMD ["python", "library_app_integration.py"]
COPY app.py .

