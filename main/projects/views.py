import sys
sys.path.append("..")
from django.shortcuts import render, redirect
from .models import Projects
from customuser.models import Customuser
from django.core.paginator import Paginator

# Create your views here.
def dashboard(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = Customuser.objects.get(id=user_id)
        projects = Projects.objects.all()
        paginator = Paginator(projects, 3)
        page_no = request.GET.get('page')
        page_obj = paginator.get_page(page_no)

        start_index = (page_obj.number - 1) * paginator.per_page + 1
        end_index = start_index + len(page_obj.object_list) - 1

        context = {
            "user": user,
            "projects": page_obj,
            "start_index": start_index,
            "end_index": end_index,
            "total_entries": paginator.count,
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



    