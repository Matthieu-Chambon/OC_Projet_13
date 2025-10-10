# Installation & Démarrage

## Prérequis

Avant de commencer, assurez-vous d’avoir installé :

- **Python 3.12**

  → Vérifiez l’installation avec :

  ```bash
  python --version
  ```
- **Docker**

  → Vérifiez l'installation avec :

  ```bash
  docker --version
  ```
- Un compte sur :

  - **GitHub** – pour cloner le dépôt et accéder au code source
  - **Docker Hub** – pour stocker et récupérer les images Docker
  - **Render** – pour le déploiement en ligne

## Installation locale (sans Docker)

Clonez le projet et installez les dépendances nécessaires :

### 1. Cloner le dépôt GitHub

```console
git clone https://github.com/matthieu-chambon/oc_projet_13.git
cd oc_projet_13
```

### 2. Créer et activer un environnement virtuel

Sous **macOS / Linux** :

```console
python -m venv venv
source venv/bin/activate
```

Sous **Windows** :

```console
python -m venv venv
venv\Scripts\activate
```


### 3. Installer les dépendances Python

```console
pip install -r requirements.txt
```


### 4. (Optionnel) Collecter les fichiers statiques

Si votre fichier `.env` contient la ligne suivante :

```
DJANGO_DEBUG=False
```

vous devez exécuter cette commande avant de lancer le serveur :

```console
python manage.py collectstatic --noinput
```

Cela permet à Django de regrouper tous les fichiers statiques (CSS, JS, images) dans un dossier unique afin qu’ils soient servis correctement en mode production.


### 5. Lancer le serveur local

```console
python manage.py runserver
```

L’application est maintenant accessible à l’adresse [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Lancement en local avec Docker

Il est également possible d'exécuter l’application dans un conteneur :

### 1. Construire l’image Docker

```bash
docker build -t oc_projet_13 .
```

### 2. Lancer le conteneur

```bash
docker run -d -p 8000:8000 oc_projet_13
```

L’application est maintenant accessible à l’adresse [http://localhost:8000/](http://localhost:8000/)