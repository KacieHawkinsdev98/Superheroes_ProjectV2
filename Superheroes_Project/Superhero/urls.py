from . import views
from django.urls import path


app_name = 'Superhero'
urlpatterns = [
    path('', views.index, name=''),
    path('<int:superheros_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create_new_superheros'),
    path('edit/<superheros_id>/', views.edit, name='edit_superheros'),
    path('delete/<superheros_id>/', views.delete, name='delete_superheros')

]