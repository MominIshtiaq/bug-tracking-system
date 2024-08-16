from django.http import HttpResponse
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Customuser
from .forms import SignUpForm, LogInForm
from django.views.generic.edit import CreateView, FormView


def index(request):
    if not request.session.get("user_id"):
        return render(request, 'customuser/index.html')
    else:
        return redirect('projects:dashboard')

def signup_redirect(request):
    return redirect('customuser:index')

def signup(request, actor=None):
    if actor is None:
        return redirect('customuser:index')
    if not request.session.get('user_id'):
        form = SignUpForm()
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                email = form.cleaned_data['email']
                if Customuser.objects.filter(email=email).exists():
                    form.add_error('email', 'Email already exists')
                else:
                    userType = actor
                    password = form.cleaned_data['password']
                    user = Customuser(
                        username=name, 
                        password=password, 
                        email=email, 
                        user_type=userType
                    )
                    user.save()
                    return redirect("customuser:login")
        
        context = {'form': form}
        return render(request, 'customuser/signin.html', context)
    else:
        return redirect('projects:dashboard')

class SignUpView(CreateView):
    model = Customuser
    form_class = SignUpForm
    template_name = 'customuser/signin.html'
    success_url = reverse_lazy('customuser:login')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        if Customuser.objects.filter(email=email).exists():
            form.add_error('email', 'A user with this email already exists.')
            return self.form_invalid(form)
        
        form.instance.user_type = self.kwargs['actor']
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
    
class LoginView(FormView):
    template_name = 'customuser/login.html'
    form_class = LogInForm
    success_url = reverse_lazy('projects:dashboard')

    def dispatch(self, request, *args, **kwargs):
        if request.session.get('user_id'):
            return redirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try:
            user = Customuser.objects.get(email=email)
            if form.cleaned_data['username'] == user.username and password == user.password:
                self.request.session['user_id'] = user.id
                return redirect(self.get_success_url())
            else:
                form.add_error(None, "Invalid username or password")
        except Customuser.DoesNotExist:
            form.add_error(None, "User with this email does not exist")
        
        return self.form_invalid(form)


def login(request):
    user_id = request.session.get('user_id')
    if not user_id:
        form = LogInForm()
        if request.method == "POST":
            form = LogInForm(request.POST)
            email = request.POST.get("email")
            user = Customuser.objects.get(email = email)
            print(user)
            
            if form.is_valid():
                name = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']

                if(name == user.username and email == user.email and password == user.password):
                    request.session['user_id'] = user.id
                    return redirect('projects:dashboard')
                
        context = {'form': form}

        return render(request, 'customuser/login.html', context)
    else:
        return redirect('projects:dashboard')



def logout(request):
    request.session.flush()
    return redirect('customuser:login')
