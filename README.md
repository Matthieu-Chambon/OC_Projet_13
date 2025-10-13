# Projet 13 - Mettez à l'échelle une application Django en utilisant une architecture modulaire

## 📚 Description

Ce projet **OC Lettings** a pour objectif de moderniser et automatiser le déploiement d’une application Django via une architecture modulaire basée sur Docker et GitHub Actions.

Fonctionnalités principales :
- Gestion d’annonces de **locations immobilières**
- Application **Django** conteneurisée avec **Docker**
- Tests automatisés et **vérification de la qualité du code**
- **Pipeline CI/CD** complète via **GitHub Actions**
- **Déploiement automatique** sur **Render**
- Suivi des erreurs et logs via **Sentry**

## 📥 Installation et exécution

```bash
git clone https://github.com/matthieu-chambon/oc_projet_13.git
cd oc_projet_13
```

### 2. Créer l’environnement virtuel

```bash
python -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate     # Windows
```

### 3. Installer les dépendances

```bash
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

```bash
python manage.py runserver
```

L’application est maintenant accessible à [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## 🐳 Exécution avec Docker

```bash
docker build -t oc_projet_13 .
docker run -d -p 8000:8000 oc_projet_13
```

## 🔑 Accès au panneau d’administration

Une fois l’application en cours d’exécution, vous pouvez accéder à l’interface d’administration Django : [http://localhost:8000/admin](http://localhost:8000/admin)

### Identifiants par défaut
- **Utilisateur :** `admin`  
- **Mot de passe :** `Abc1234!`

Depuis cette interface, il est possible de :
  - Ajouter ou modifier une **location** (`Letting`)
  - Gérer les **adresses** associées (`Address`)
  - Administrer les **profils utilisateurs** (`Profile`)

## 🔁 CI/CD & Déploiement

Le pipeline CI/CD (GitHub Actions) automatise les étapes suivantes :

1. Installation de **Python** et des **dépendances**
2. Exécution des **tests** et du **linter** (Flake8)
3. Construction et publication de l’image Docker sur **Docker Hub**
4. Déclenchement du déploiement automatique sur **Render**

> ⚠️ Le déploiement Render ne s’exécute que sur la branche `master`.

### 🔐 Secrets GitHub utilisés

| Nom du secret        | Description                                      |
| -------------------- | ------------------------------------------------ |
| `DOCKERHUB_USERNAME` | Nom d’utilisateur Docker Hub                     |
| `DOCKERHUB_TOKEN`    | Token d’accès Docker Hub                         |
| `RENDER_DEPLOY_HOOK` | URL du webhook Render déclenchant le déploiement |

## 🛠️ Technologies principales

- [Python 3.12](https://www.python.org/)
- [Django 3.0](https://docs.djangoproject.com/en/3.0/)
- [Docker](https://docs.docker.com/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Render](https://render.com/docs)
- [Sentry](https://docs.sentry.io/)
- [Read the Docs](https://readthedocs.org/)
- [pytest](https://docs.pytest.org/)

## 📖 Documentation complète

Une documentation technique complète est disponible sur **Read the Docs** :
 [https://oc-projet-13.readthedocs.io/](https://oc-projet-13.readthedocs.io/)

Elle détaille :

- la structure du projet
- les modèles de données
- le pipeline CI/CD
- les tests de couverture de code et de qualité
- la configuration de Sentry
- les étapes de déploiement