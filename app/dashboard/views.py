from django.shortcuts import render

# TODO aprender vistas basadas en clases
from django.views import View

# Create your views here.
def home_view(request):
    context = {}
    return render(request, "index.html", context)
