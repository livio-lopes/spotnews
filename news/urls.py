from django.urls import path
from news.views import index, details_page, add_categories, add_news


urlpatterns = [
    path("", index, name="home-page"),
    path("<int:id>/", details_page, name="news-details-page"),
    path("categories/", add_categories, name="categories-form"),
    path("news/", add_news, name="news-form"),
]
