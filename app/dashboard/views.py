from django.shortcuts import render

# TODO aprender vistas basadas en clases
from django.views import View

# Create your views here.
def home_view(request):
    """Vista home

    Args:
        request (request): Recibe un request

    Returns:
        render: Devuelve un método render con el html y contexto
    """
    context = {}
    return render(request, "dashboard/index.html", context)
