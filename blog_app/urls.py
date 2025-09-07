from django.urls import path
from . import views

app_name = "blog_app"

urlpatterns = [
    path("", views.index, name="home"),  # главная страница
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),  # детальная страница поста
    path("category/<slug:slug>/", views.category_detail, name="category_detail"),  # посты по категории
    path("categories/", views.category_list, name="category_list"),  # 👈 добавляем
    path("tag/<slug:slug>/", views.tag_detail, name="tag_detail"),  # посты по тегу
    path("about/", views.about, name="about"),  # статическая страница "О блоге"
]
