from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Superhero'
urlpatterns = [
    path('', views.index, name=''),
    path('<int:superhero_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create_new_superhero'),
    path('edit/<superhero_id>/', views.edit, name='edit_superhero'),
    path('delete/<superhero_id>/', views.delete, name='delete_superhero')

]