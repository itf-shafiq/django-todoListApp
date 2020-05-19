from django.urls import path
from .import views

# Create Path here 

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('delete/<TaskList_id>', views.delete, name="delete"),
    path('completed/<TaskList_id>', views.completed, name="completed"),
    path('uncompleted/<TaskList_id>', views.uncompleted, name="uncompleted"),
    path('edit/<TaskList_id>', views.edit, name="edit")

]