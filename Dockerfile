# Utilise une image Python officielle
FROM python:3.12-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers de dépendances
COPY requirements.txt .

# Installe les dépendances
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copie tout le projet dans le conteneur
COPY . .

# Collecte les fichiers statiques pour la prod
RUN python manage.py collectstatic --noinput

# Expose le port sur lequel Django tournera
EXPOSE 8000

# Commande pour lancer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
