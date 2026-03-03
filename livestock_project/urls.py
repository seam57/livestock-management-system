from django.contrib import admin
from django.urls import path
from farm import views  # Views ke import kora hoyeche

urlpatterns = [
    # Admin Panel Path
    path('admin/', admin.site.urls),
    
    # Dashboard (Home) Path
    path('', views.dashboard, name='dashboard'), 
    
    # Add Animal Path - Eta thaklei button kaj korbe
    path('add/', views.add_animal, name='add_animal'), 
]