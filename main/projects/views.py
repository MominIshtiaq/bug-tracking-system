import sys
sys.path.append("..")
from django.shortcuts import render, redirect
from .models import Projects
from customuser.models import Customuser

# Create your views here.
def dashboard(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = Customuser.objects.get(id=user_id)
        projects = Projects.objects.all()
        context = {
            "user": user,
            "projects": projects
        }
    else:
        return redirect('customuser:login')
    
    return render(request, 'projects/dashboard.html', context)

def createproject(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        if user_id:
            user = Customuser.objects.get(id=user_id)
            project_name = request.POST.get('projectName')
            short_details = request.POST.get('shortDetails')
            project = Projects(manager=user, name=project_name, detail=short_details)
            project.save()
            
            return redirect('projects:dashboard')
    else:
        return redirect('projects:dashboard')

def logout(request):
    request.session.flush()
    return redirect('customuser:login')

    