from . import views
from django.urls import path



app_name = 'Superhero'
urlpatterns = [
    path('', views.index, name='index'),
    path('details/', views.detail, name='detail'),
    path('new/', views.create, name='create_new_superheros'),
    path('edit/', views.edit, name='edit_superheros'),
    path('delete/', views.delete, name='delete_superheros')
 
]