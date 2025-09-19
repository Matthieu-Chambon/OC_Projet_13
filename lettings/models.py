from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Modèle représentant une adresse postale

    Args:
        models (Model): Classe de base pour tous les modèles Django

    Fields:
        number (PositiveIntegerField): Numéro de la rue (max 4 chiffres)
        street (CharField): Nom de la rue (max 64 caractères)
        city (CharField): Nom de la ville (max 64 caractères)
        state (CharField): Code de l'état (2 caractères)
        zip_code (PositiveIntegerField): Code postal (max 5 chiffres)
        country_iso_code (CharField): Code ISO du pays (3 caractères)
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Modèle représentant une location

    Args:
        models (Model): Classe de base pour tous les modèles Django

    Fields:
        title (CharField): Titre de la location (max 256 caractères)
        address (OneToOneField): Relation un-à-un avec le modèle Address
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
