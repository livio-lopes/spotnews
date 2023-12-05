from django.shortcuts import render
from news.models import News, Category


# Create your views here.
def index(request):
    context = {"title": "Página Inicial", "news": News.objects.all()}
    return render(request, "home.html", context)


def details_page(request, id):
    get_news = News.objects.get(id=id)
    get_categories = Category.objects.get(id=get_news.id)
    context = {
        "title": "Página de Detalhes da Notícia",
        "report": get_news,
        "categories": get_categories.name,
    }
    return render(request, "news_details.html", context)
