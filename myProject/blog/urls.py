from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name="index"),
    path('post/<slugInput>', views.detailPost, name='detail'),
    path('category/<categoryInput>', views.categoryPost, name='category'),
]
