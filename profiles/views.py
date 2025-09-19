from django.shortcuts import render
from profiles.models import Profile


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
    profiles_list = Profile.objects.all()
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
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
