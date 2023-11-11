from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html', {'nav_item': 'home'})

def about(request):
    return render(request,'pages/about.html', {'nav_item': 'about'})

def resume(request):
    return render(request,'pages/resume.html', {'nav_item': 'resume'})

def portfolio(request):
    return render(request,'pages/portfolio.html', {'nav_item': 'portfolio'})

def services(request):
    return render(request,'pages/services.html', {'nav_item': 'services'})

def contacts(request):
    return render(request,'pages/contacts.html', {'nav_item': 'contacts'})