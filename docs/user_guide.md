# Guide d’utilisation

## Fonctionnalités principales

L’application **OC Lettings** permet :

- d’afficher la **liste des locations** disponibles
- de consulter le **détail d’une location** (adresse, titre, etc.)
- d’afficher la **liste des profils utilisateurs**
- de consulter le **profil détaillé** d’un utilisateur (nom, ville préférée)
- et pour les administrateurs, de **gérer les données** via l’interface `/admin/`

Une fois l’application lancée (voir la partie [Installation](installation)), vous serez redirigé vers la **page d’accueil** du site.

## Cas d’utilisation

### 1. Consulter les profils utilisateurs

- Accédez à **/profiles/** ou cliquez sur "Profiles" depuis la page d'accueil
- Une liste de tous les utilisateurs enregistrés s'affiche
- Cliquez sur un nom d'utilisateur pour voir ses **détails** (prénom, nom, etc .)

**Résultat attendu :** Cette partie du site affiche les informations des différents profils enregistrées dans la base de données.

### 2. Consulter la liste des locations

- Accédez à **/lettings/** ou cliquez sur "Lettings" depuis la page d’accueil
- Une liste de toutes les locations disponibles s’affiche
- Cliquez sur une location pour voir ses **détails** (titre, adresse complète, etc .)

**Résultat attendu :** Cette partie du site détaille toutes les informations liées aux locations.

### 3. Gérer les données

- Connectez-vous à **/admin/** (nécessite un compte administrateur Django).
- Vous pouvez alors :

  - Ajouter ou modifier une **location** (`Letting`)
  - Gérer les **adresses** associées (`Address`)
  - Administrer les **profils utilisateurs** (`Profile`)

**Résultat attendu :** les modifications sont automatiquement enregistrées dans la base de données.

Si aucun compte **administrateur** n'a été créé, il est possible de créer un **superutilisateur** via la commande :

```bash
python manage.py createsuperuser
```
