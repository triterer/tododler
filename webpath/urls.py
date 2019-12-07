from django.urls import path

from . import views
app_name = 'webpath'
urlpatterns = [
    
    path('registration/', views.reguser),
    path('login/', views.loguser),
    path('createmes/',views.create_new),
    path('allpage/', views.showall, name="showall")
]
