from django.shortcuts import render
from lettings.models import Letting
from django.http import Http404
import sentry_sdk
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit. Sed non placerat
# massa. Integer est nunc, pulvinar a tempor et, bibendum id arcu. Vestibulum ante ipsum primis in
# faucibus orci luctus et ultrices posuere cubilia curae; Cras eget scelerisque
def index(request):
    """
    Vue pour la page listant toutes les locations

    Args:
        request (HttpRequest): Objet représentant la requête HTTP

    Returns:
        Render de la page HTML avec la liste des locations
    """
    try:
        logger.info("Récupération des locations depuis la base de données")
        lettings_list = Letting.objects.all()

    except Exception as e:
        logger.exception("Erreur lors de la récupération des locations : %s", e)
        sentry_sdk.capture_exception(e)
        lettings_list = []

    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan porta nisl id
# eleifend. Praesent dignissim, odio eu consequat pretium, purus urna vulputate arcu, vitae
# efficitur lacus justo nec purus. Aenean finibus faucibus lectus at porta. Maecenas auctor, est
# ut luctus congue, dui enim mattis enim, ac condimentum velit libero in magna. Suspendisse
# potenti. In tempus a nisi sed l.aoreet. Suspendisse porta dui eget sem accumsan interdum. Ut quis
# urna pellentesque justo mattis ullamcorper ac non tellus. In tristique mauris eu velit fermentum,
# tempus pharetra est luctus. Vivamus consequat aliquam libero, eget bibendum lorem. Sed non dolor
# risus. Mauris condimentum auctor elementum. Donec quis nisi ligula. Integer vehicula tincidunt
# enim, ac lacinia augue pulvinar sit amet.
def letting(request, letting_id):
    """
    Vue pour la page détaillant une location spécifique

    Args:
        request (HttpRequest): Objet représentant la requête HTTP
        letting_id (int): ID de la location à afficher

    Returns:
        Render de la page HTML avec les détails de la location
    """
    try:
        logger.info("Récupération de la location avec ID %d depuis la base de données", letting_id)
        letting = Letting.objects.get(id=letting_id)

    except Letting.DoesNotExist:
        logger.warning("Location avec ID %d non trouvée", letting_id)
        raise Http404("Location introuvable")

    except Exception as e:
        logger.exception("Erreur inattendue dans la vue letting : %s", e)
        sentry_sdk.capture_exception(e)
        return render(request, "500.html", status=500)

    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
