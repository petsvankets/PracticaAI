# Usar una imagen base de Python
FROM python:3.8-slim

# Instalar dependencias para compilar ciertas bibliotecas de Python
RUN apt-get update && apt-get install -y \
    build-essential \
    libxml2-dev \
    libxslt-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar las bibliotecas de Python necesarias
RUN pip install --no-cache-dir numpy matplotlib wordcloud nltk lxml requests

# Establece el directorio de trabajo
WORKDIR /app

# Copiar el código del cliente GROBID al contenedor
COPY . /app

# Asumiendo que example.py es tu script principal
CMD ["python", "example.py"]
