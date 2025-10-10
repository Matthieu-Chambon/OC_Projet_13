# Architecture & Modèles

## Structure du projet

Le projet suit une **architecture Django modulaire** :
Chaque application (`lettings`, `profiles`) est autonome et peut être réutilisée ou remplacée sans impacter les autres.

- `oc_lettings_site` agit comme le **noyau du projet** : configuration, routage global, intégration des apps
- Les apps Django (`lettings`, `profiles`) contiennent leur propre :

  - modèle (`models.py`)
  - vue (`views.py`)
  - templates
  - tests

Cela favorise la **scalabilité**, la **maintenance** et le **déploiement indépendant** des modules.

```text
.
│   .env                      ← Variables d’environnement
│   .gitignore                ← Fichiers et dossiers exclus du dépôt Git
│   .readthedocs.yaml         ← Configuration de ReadTheDocs
│   conftest.py               ← Configuration Pytest
│   Dockerfile                ← Construction de l’image Docker de l’application
│   manage.py                 ← Point d’entrée principal du projet Django
│   README.md                 ← Présentation générale du projet
│   requirements.txt          ← Liste des dépendances Python
│   setup.cfg                 ← Configuration des outils (pytest, flake8, coverage)
│
├───docs/                     ← Documentation
│   ├── conf.py               ← Configuration Sphinx
│   └── index.rst             ← Page d’entrée de la documentation
│
├───oc_lettings_site/         ← Application principale Django
│   ├── settings.py           ← Configuration globale du projet
│   ├── urls.py               ← Routage global
│   ├── wsgi.py / asgi.py     ← Points d’entrée serveur
│   └── tests/                ← Tests de l'application principale
│
├───lettings/                 ← Application "lettings"
│   ├── models.py             ← Modèles de l'app (Address + Letting)
│   ├── views.py              ← Logique métier et vues
│   ├── templates/lettings/   ← Templates HTML de l'app
│   └── tests/                ← Tests dédiés à l’app
│
├───profiles/                 ← Application "profiles"
│   ├── models.py             ← Modèles de l'app (Profile)
│   ├── views.py              ← Gestion des pages de profil
│   ├── templates/profiles/   ← Templates HTML de l'app
│   └── tests/                ← Tests dédiés à l’app
│
├───templates/                ← Templates globaux du projet
│   ├── base.html
│   ├── index.html
│   └── 404.html / 500.html
│
├───static/                   ← Fichiers CSS, JS et images sources
│   ├── assets/
│   ├── css/
│   └── js/
│
└───staticfiles/              ← Fichiers statiques collectés (via collectstatic)
```

## Structure de la base de données et des modèles de données

L’application repose sur trois modèles (**Profile**, **Address**, **Letting**) répartis dans les deux applications.

Ces modèles sont stockés dans une base de données SQLite en local (`oc-lettings-site.sqlite3`).

### Application **profiles**

#### Modèle **Profile**

Représente le profil étendu d’un utilisateur Django.

| Champ           | Type Django                          | Description                                |
| --------------- | ------------------------------------ | ------------------------------------------ |
| `user`          | OneToOneField(User)                  | Relation un-à-un avec le modèle User natif |
| `favorite_city` | CharField(max_length=64, blank=True) | Ville favorite, champ optionnel            |

**Relations :**
Un modèle `Profile` est lié à **un seul utilisateur Django natif** (`User`) (relation *One-to-One*).

### Application **lettings**

#### Modèle **Address**

Représente une adresse postale complète.

| Champ              | Type Django              | Validation               | Description                  |
| ------------------ | ------------------------ | ------------------------ | ---------------------------- |
| `number`           | PositiveIntegerField     | max=9999                 | Numéro de la rue             |
| `street`           | CharField(max_length=64) |                          | Nom de la rue                |
| `city`             | CharField(max_length=64) |                          | Nom de la ville              |
| `state`            | CharField(max_length=2)  | longueur exacte = 2      | Code de l'état               |
| `zip_code`         | PositiveIntegerField     | max=99999                | Code postal                  |
| `country_iso_code` | CharField(max_length=3)  | longueur exacte = 3      | Code ISO du pays             |

**Relations :**
Un modèle `Address` est lié à **une seule location** (`Letting`) (relation *One-to-One*).

#### Modèle **Letting**

Représente une location immobilière.

| Champ     | Type Django               | Description                             |
| --------- | ------------------------- | --------------------------------------- |
| `title`   | CharField(max_length=256) | Titre de la location                    |
| `address` | OneToOneField(Address)    | Relation un-à-un avec le modèle Address |

**Relations :**
Un modèle `Letting` est lié à **une seule adresse** (`Address`) (relation *One-to-One*).

## Technologies utilisées

Le projet repose sur plusieurs briques techniques :

### Backend

- **[Python 3.12](https://www.python.org/doc/)** – Langage principal
- **[Django 3.0](https://docs.djangoproject.com/en/3.0/)** – Framework web principal
- **[Whitenoise](https://whitenoise.evans.io/en/stable/)** – Gestion des fichiers statiques en production
- **[Sentry SDK](https://docs.sentry.io/platforms/python/guides/django/)** – Suivi et gestion des erreurs en production
- **[pytest](https://docs.pytest.org/en/stable/)** / **[pytest-django](https://pytest-django.readthedocs.io/en/latest/)** / **[pytest-cov](https://pytest-cov.readthedocs.io/en/latest/)** – Tests unitaires, d'intégration et de couverture

### Conteneurisation et déploiement

- **[Docker](https://docs.docker.com/)** – Conteneurisation de l'application
- **[Render](https://render.com/docs)** – Hébergement et déploiement de l'application
- **[GitHub Actions](https://docs.github.com/en/actions)** – Pipeline CI/CD et déploiement continu

### Documentation

- **[Sphinx](https://www.sphinx-doc.org/en/master/)** + **[MyST Parser](https://myst-parser.readthedocs.io/en/latest/)** – Documentation au format Markdown
- **[Read the Docs](https://docs.readthedocs.io/en/stable/)** – Hébergement et génération automatique de la documentation

## Interfaces de programmation

### Vue d’ensemble

L’application **OC Lettings** s’appuie sur le framework **Django** pour gérer les échanges entre le serveur et l’utilisateur via des **vues** et des **templates HTML**.

Les interfaces de programmation se présentent donc sous la forme :

- de **fonctions de vue** (`views.py`) côté serveur
- associées à des **URL** définies dans `urls.py`
- et de **templates HTML** qui restituent les données au navigateur

### Structure des routes principales

| URL                       | Vue associée                     | Description                     |
| ------------------------- | -------------------------------- | ------------------------------- |
| `/`                       | `oc_lettings_site.views.index`   | Page d’accueil                  |
| `/lettings/`              | `lettings.views.index`           | Liste des locations             |
| `/lettings/<letting_id>/` | `lettings.views.letting`         | Détails d’une location          |
| `/profiles/`              | `profiles.views.index`           | Liste des profils utilisateurs  |
| `/profiles/<username>/`   | `profiles.views.profile`         | Détails d’un profil utilisateur |
| `/admin/`                 | `django.contrib.admin.site.urls` | Interface d’administration      |


Chaque vue utilise ensuite un **template HTML** (dans dossier `templates/` de chaque application).

Des pages d’erreur personnalisées (`404.html`, `500.html`) sont églament fournies dans le dossier `templates/` à la racine du projet.