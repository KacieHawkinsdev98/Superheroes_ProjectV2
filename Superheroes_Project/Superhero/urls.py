from . import views
from django.urls import path



app_name = 'Superhero'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail', views.detail, name='detail'),
    path('create', views.create, name='create'),
    path('edit', views.edit, name='edit'),
    path('delete', views.delete, name='delete')
 
]