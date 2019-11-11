from django.urls import path

from . import views
app_name = 'descpath'
urlpatterns = [
    
    path('registration/', views.registration),
    path('login/', views.authentification),
    path('nm/',views.create_mes)
]
