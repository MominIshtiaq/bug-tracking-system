import sys
sys.path.append("..")
from django.shortcuts import render, redirect
from .models import Projects
from customuser.models import Customuser
from django.core.paginator import Paginator

# import json
# from django.conf import settings
# from django.http import JsonResponse

# Create your views here.
def dashboard(request):
    user_id = request.session.get('user_id')
    user = Customuser.objects.get(id=user_id)
    if user:
        projects = Projects.objects.all()
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
    # query = request.GET.get('query', '')
    # if query:
    #     projects = Projects.objects.filter(name__icontains=query)
    #     print(projects)
    # else:
    #     projects = Projects.objects.all()  # Return all projects if query is empty

    # results = []
    # for project in projects:
    #     project_data = {
    #         'name': project.name,
    #         'detail': project.detail,
    #         'image': project.image.url,
    #         'url': project.get_absolute_url()
    #     }
    #     results.append(project_data)

    # print(results)
    # return JsonResponse({'results': results})


    