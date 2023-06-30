from django.urls import path
from django.views.decorators.cache import cache_page

from dogs.views import index, categories, DogListView, DogCreateView, DogUpdateView
from dogs.apps import DogsConfig

app_name = DogsConfig.name

urlpatterns = [
    path('', cache_page(60)(index), name='index'),
    path('categories/', categories, name='categories'),
    path('<int:pk>/dogs/', DogListView.as_view(), name='category_dogs'),
    path('<int:pk>/dogs/create/', DogCreateView.as_view(), name='dog_create'),
    path('dogs/<int:pk>/update/', DogUpdateView.as_view(), name='dog_update')
]
