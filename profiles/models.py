from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Modèle représentant le profil utilisateur

    Args:
        models (Model): Classe de base pour tous les modèles Django

    Fields:
        user (OneToOneField): Relation un-à-un avec le modèle User
        favorite_city (CharField): Ville favorite (max 64 caractères, peut être vide)
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
