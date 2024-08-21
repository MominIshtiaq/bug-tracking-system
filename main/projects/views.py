import sys
sys.path.append("..")
from django.shortcuts import render, redirect
from .models import Projects
from customuser.models import Customuser
from django.core.paginator import Paginator

# import json
# from django.conf import settings
# from django.http import JsonResponse

def dashboard(request):
    user_id = request.session.get('user_id')
    user = Customuser.objects.get(id=user_id)
    if user:
        projects = Projects.objects.all()

        for project in projects:
            bugs_list = project.bugs.all()
            project.bugs_count = len(bugs_list)
            project.bugs_completed = 0
            for bug in bugs_list:
                if bug.status == "completed" or bug.status == 'resolved':
                    project.bugs_completed += 1

        search_input = request.POST.get('search-input')
        if search_input:
            projects = Projects.objects.filter(name__icontains=search_input)
        
        paginator = Paginator(projects, 3)
        page_no = request.GET.get('page')
        page_obj = paginator.get_page(page_no)

        start_index = (page_obj.number - 1) * paginator.per_page + 1
        end_index = start_index + len(page_obj.object_list) - 1

        # projects_data = list(Projects.objects.values())
        # for project in projects_data:
        #     project['image'] = settings.MEDIA_URL + project['image']

        context = {
            "user": user,
            "projects": page_obj,
            "start_index": start_index,
            "end_index": end_index,
            "total_entries": paginator.count,
            # "qs_json": json.dumps(projects_data) to dump all the data received from the database to the DOM
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

def search_view(request):
    if request.method == 'POST':
        search_input = request.POST.get('search-input')
        if search_input:
            projects = Projects.objects.filter(name__icontains=search_input)
            context = {
                "projects": projects,
            }
            return render(request, 'projects/search.html', context)
    return redirect('projects:dashboard')

def error_404_view(request, exception):
    return render(request, '404.html', status=404)