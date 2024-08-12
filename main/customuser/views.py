from django.shortcuts import render, redirect
from .models import Customuser
from .forms import SignInForm, LogInForm

def index(request):
    return render(request, 'customuser/index.html')


def signin(request, actor):
    form = SignInForm()
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            email = form.cleaned_data['email']
            userType = actor
            password = form.cleaned_data['password']
            user = Customuser(username = name, password = password,  email = email, user_type = userType)
            user.save()
            return redirect("customuser:login")
    
    context = {'form': form}

    return render(request, 'customuser/signin.html', context)

def login(request):
    form = LogInForm()
    if request.method == "POST":
        form = LogInForm(request.POST)
        email = request.POST.get("email")
        userEmail = Customuser.objects.get(email = email)
        

        if form.is_valid():
            formName = form.cleaned_data['username']
            formEmail = form.cleaned_data['email']
            formPassword = form.cleaned_data['password']

            if(formName == userEmail.username and formEmail == userEmail.email and formPassword == userEmail.password):
                user = {
                    'username': userEmail.username,
                    'email': userEmail.email,
                    'user_type': userEmail.user_type
                }
                return redirect('projects:dashboard')
            
    context = {'form': form}

    return render(request, 'customuser/login.html', context)