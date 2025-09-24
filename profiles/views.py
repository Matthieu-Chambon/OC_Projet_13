from django.shortcuts import render
from profiles.models import Profile
from django.http import Http404
import sentry_sdk
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat libero
# pulvinar eget. Fusc faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum
# lacus d
def index(request):
    """
    Vue pour la page listant tous les profils

    Args:
        request (HttpRequest): Objet représentant la requête HTTP

    Returns:
        Render de la page HTML avec la liste des profils
    """
    try:
        logger.info("Récupération des profils depuis la base de données")
        profiles_list = Profile.objects.all()

    except Exception as e:
        logger.exception("Erreur lors de la récupération des profils : %s", e)
        sentry_sdk.capture_exception(e)
        profiles_list = []

    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt, dolor
# id facilisis fringilla, eros leo tristique lacus, it. Nam aliquam dignissim congue. Pellentesque
# habitant morbi tristique senectus et netus et males.
def profile(request, username):
    """
    Vue pour la page détaillant un profil spécifique

    Args:
        request (HttpRequest): Objet représentant la requête HTTP
        username (str): Nom d'utilisateur du profil à afficher

    Returns:
        Render de la page HTML avec les détails du profil
    """
    try:
        logger.info(
            "Récupération du profil pour l'utilisateur '%s' depuis la base de données",
            username
        )
        profile = Profile.objects.get(user__username=username)

    except Profile.DoesNotExist:
        logger.warning("Profil avec nom d'utilisateur '%s' non trouvé", username)
        raise Http404("Profil introuvable")

    except Exception as e:
        logger.exception("Erreur inattendue dans la vue profile : %s", e)
        sentry_sdk.capture_exception(e)
        return render(request, "500.html", status=500)

    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
