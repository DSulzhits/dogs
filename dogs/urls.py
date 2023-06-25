from django.urls import path

from dogs.views import index, categories, DogListView, DogCreateView, DogUpdateView
from dogs.apps import DogsConfig

app_name = DogsConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('<int:pk>/dogs/', DogListView.as_view(), name='category_dogs'),
    path('<int:pk>/dogs/create/', DogCreateView.as_view(), name='dog_create'),
    path('dogs/<int:pk>/update/', DogUpdateView.as_view(), name='dog_update')
]
