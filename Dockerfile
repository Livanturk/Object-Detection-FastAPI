# Temel Python imajı
FROM python:3.11-slim

# Gerekli sistem paketleri
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev


# Çalışma dizini
WORKDIR /app

# Uygulama dosyalarını kopyala
COPY app/ ./app/

# Gerekli paketleri yükle
RUN pip install --no-cache-dir -r app/requirements.txt

# Portu dışa aç
EXPOSE 8000

# Uygulamayı çalıştır
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
