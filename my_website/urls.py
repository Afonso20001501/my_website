
from django.urls import path
from my_website import views

app_name = 'my_website'

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('projects/', views.Projects.as_view(), name="projects"),
    path('resume/', views.Resume.as_view(), name="resume"),
    path('contact/', views.Contact.as_view(), name="contact"),
]
