from . import views
from django.urls import path



app_name = 'Superhero'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:superheros_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('delete/<superheros_id>/', views.delete, name='delete')
 
]