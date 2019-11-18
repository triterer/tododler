from django.urls import path

from . import views
app_name = 'descpath'
urlpatterns = [
    
    path('registration/', views.reguser),
    path('login/', views.loguser),
    #path('nm/',views.create_mes),
    path('allpage/', views.show_all)
]
