from django.shortcuts import render
from basicapp.forms import UserEntryForm, UserProfileForm

#more views

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')

def register(request):
    registered = False
    
    if request.method == "POST":
        user_entry_form = UserEntryForm(data = request.POST)
        user_profile_form = UserProfileForm(data = request.POST)
        
        
        if user_entry_form.is_valid() and user_profile_form.is_valid():
            
            user = user_entry_form.save()
            user.set_password(user.password)
            user.save()
        
            profile = user_profile_form.save(commit=False)
            profile.user = user
            
            if 'Profile_Pic' in request.FILES:
                profile.Profile_Pic = request.FILES['Profile_Pic']
            
            profile.save()
        
            registered = True
        else:
            print(user_entry_form.errors,user_profile_form.errors)
    else:
        user_entry_form = UserEntryForm()
        user_profile_form = UserProfileForm()
        
    return render(request,'basicApp/registration.html',
                 {'UserEntryForm':user_entry_form,
                  'UserProfileForm':user_profile_form,
                  'registered':registered })

@login_required
def special(request):
    return HttpResponse('You are Logged In')


@login_required
def user_logout(request):
    logout(request)
    HttpResponseRedirect(reverse('index'))
    
def user_login(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate (username = username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account Not Active')
        else:
            print('Someone tried to login but failed')
            print('Username:{} and Password: {}'.format(username, password))
            return HttpResponse("Invalid Log In Details")
    else:
        return render(request,'basicapp/login.html')
            
    
    
    
    
    