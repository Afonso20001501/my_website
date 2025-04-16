from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class Home(TemplateView):
    template_name = 'my_website/pages/index.html'
    
class Projects(TemplateView):
    template_name = 'my_website/pages/projects.html'
    
class Resume(TemplateView):
    template_name = 'my_website/pages/resume.html'

class Contact(TemplateView):
    template_name = 'my_website/pages/contact.html'