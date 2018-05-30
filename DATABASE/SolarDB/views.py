from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import User

# Create your views here.
def index(request):
    

    context = {}
    if request.method == "POST":
        if 'login' in request.POST:
            try:
                user = User.objects.get(username=request.POST['username'], password=request.POST['password'])

                request.session['user'] = user.pk
                #request.session['type'] = user.get_type()
                return HttpResponseRedirect('homepage')

            except User.DoesNotExist:
                context['log_error'] = 'Cannot find an account with that combination.'
                
    return render(request, 'login.html')

def register(request):
    context = {}
    if 'register' in request.POST:
            try:
                user = User.objects.get(username=request.POST['username'])
                context['reg_error'] = 'That username is already taken.'
            except User.DoesNotExist:
                user = User(username=request.POST['username'], password=request.POST['password']
                           )
                user.save()
                context['reg_success'] = "Account has been created."
            return HttpResponse("hi")
    return render(request, 'register.html')

def homepage(request):
    return render(request, 'homepage.html')