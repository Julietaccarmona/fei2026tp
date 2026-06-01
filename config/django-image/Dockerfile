FROM python:3.12.2-bookworm

WORKDIR /app

# copiar dependencias
COPY requirements.txt /app/requirements.txt

# instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# copiar script de arranque
COPY config/django-image/start.sh /start.sh

RUN chmod +x /start.sh

# comando de inicio del contenedor
CMD ["/start.sh"]
