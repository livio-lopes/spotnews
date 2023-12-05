from django.shortcuts import render
from news.models import News


# Create your views here.
def index(request):
    context = {"title": "Página Inicial", "news": News.objects.all()}
    return render(request, "home.html", context)


def details_page(request, id):
    get_news = News.objects.get(id=id)
    context = {
        "title": "Página de Detalhes da Notícia",
        "report": get_news,
    }
    return render(request, "news_details.html", context)
