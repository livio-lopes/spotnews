from django.shortcuts import render
from news.models import News


# Create your views here.
def index(request):
    context = {"title": "Página Inicial", "news": News.objects.all()}
    return render(request, "home.html", context)
