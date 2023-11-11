from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index' ),
    path('about/', views.about, name='about' ),
    path('resume/', views.about, name='resume' ),
    path('portfolio/', views.about, name='portfolio' ),
    path('services/', views.about, name='services' ),
    path('contacts/', views.about, name='contacts' ),
    
]
