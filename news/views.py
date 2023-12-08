from django.shortcuts import render, redirect
from news.models import News, Category
from news.forms import CreateCategoriesModelForm, CreateNewsModelForm


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


def add_categories(request):
    form = CreateCategoriesModelForm()

    if request.method == "POST":
        form = CreateCategoriesModelForm(request.POST)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect("home-page")

    context = {"title": "Formulário para Nova Categoria", "form": form}
    return render(request, "categories_form.html", context)


def add_news(request):
    form = CreateNewsModelForm()
    if request.method == "POST":
        form = CreateNewsModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home-page")

    context = {"title": "Formulário para Nova Notícia", "form": form}
    return render(request, "news_form.html", context)
