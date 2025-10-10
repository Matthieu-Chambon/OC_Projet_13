# Tests, Erreurs & Logging

## Tests et qualité

Le projet inclut :

- des **tests unitaires** et **tests d’intégration** dans chaque application
- un fichier `.coveragerc` pour **la couverture** de test
- **flake8** pour le respect de la norme PEP8

Exécuter les tests :

```bash
pytest
```

Vérifier la couverture de test :

```bash
pytest --cov
```

Vérifier le respect de la norme PEP8 :

```bash
flake8
```

## Gestion des erreurs et du logging

L’application est intégrée avec **[Sentry](https://sentry.io/)** pour assurer la **collecte, le suivi et l’analyse des erreurs** en production.

### Configuration

Dans `settings.py`, Sentry est initialisé via le SDK officiel Django :

```python
import sentry_sdk
import logging
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

sentry_logging = LoggingIntegration(
    level=logging.INFO,                # Capture tous les logs de niveau INFO ou plus
    event_level=logging.ERROR          # Envoie des événements de niveau ERROR ou plus
)

sentry_sdk.init(
    dsn=os.getenv('SENTRY_DSN', ''),   # Clé DSN stockée dans le fichier .env
    integrations=[DjangoIntegration(), sentry_logging],
    send_default_pii=True,             # Envoie d’informations utilisateur (PII)
    enable_logs=True,                  # Active la capture automatique des logs
)
```

Le **DSN** est stocké dans le fichier `.env` :

```bash
SENTRY_DSN=https://<votre_dsn_sentry>
```

### Fonctionnement

L’application utilise le module Python `logging` pour journaliser les événements tout au long de son exécution.

Exemple dans la vue qui récupère la liste des locations :

```python
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

try:
    logger.info("Récupération des locations depuis la base de données")
    lettings_list = Letting.objects.all()
except Exception as e:
    logger.exception("Erreur lors de la récupération des locations : %s", e)
    sentry_sdk.capture_exception(e)
```

Liste des différents **niveaux de log** appliqués :

-  `logger.info()` : actions normales
-  `logger.warning()` : événements inattendus mais non bloquants
-  `logger.exception()` : capture complète des erreurs

Lorsqu’une erreur se produit, Sentry enregistre automatiquement :

- le message d’erreur
- le fichier et la ligne concernés
- le contexte utilisateur
- et la liste des logs

... et remonte l'ensemble des données à **Sentry**.

Les exceptions critiques peuvent aussi être **signalées manuellement** via :

  ```python
  sentry_sdk.capture_exception(e)
  ```

Cela permet d’obtenir un suivi en temps réel des erreurs directement dans le tableau de bord Sentry.
