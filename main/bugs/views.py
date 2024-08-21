import sys
sys.path.append('..')
from django.shortcuts import render, redirect
from customuser.models import Customuser
from .models import Bug
from projects.models import Projects
from django.contrib import messages
from django.conf import settings
from django.core.files import File
import os

def bugs(request, project_id):
    user_id = request.session.get("user_id")
    dev_list = []
    assignees = []
    if user_id and project_id:
        user = Customuser.objects.get(id=user_id)
        project = Projects.objects.get(id = project_id)
        bugs = Bug.objects.filter(project = project)
        dev_objs = Customuser.objects.filter(user_type = "developer")
        for dev in dev_objs:
            dev_list.append({
                'id': dev.id,
                'username':dev.username,
            })
        for bug in bugs:
            if bug.assigned_to.username not in assignees:
                assignees.append(bug.assigned_to.username)

        context = {
            'user': user,
            'project': project,
            'dev_list': dev_list,
            'bugs': bugs,
            'assignees': assignees
        }
    else:
        return redirect("customuser:login")
    
    return render(request, "bugs/bug.html", context)

def create(request, project_id, type):
    user_id = request.session.get("user_id")
    user = None
    if user_id:
        user = Customuser.objects.get(id=user_id)
        if request.method == 'POST':
            feature_name = request.POST.get('name')
            feature_details = request.POST.get('details')
            feature_status = request.POST.get('status')
            assigned_dev_id = request.POST.get('assigned_dev')
            feature_deadline = request.POST.get('deadline')
            screenshot = request.FILES.get('formFile')
            project = Projects.objects.get(id=project_id)
            assigned_dev = Customuser.objects.get(id=assigned_dev_id)

            new_feature = Bug(
                project=project,
                created_by=user,
                assigned_to=assigned_dev,
                title=feature_name,
                description=feature_details,
                deadline=feature_deadline,
                type=type,
                status=feature_status,
            )

            if screenshot:
                new_feature.screenshot = screenshot
            else:
                default_image_path = os.path.join(settings.MEDIA_ROOT, 'screenshots', 'project_bug.jpeg')
                with open(default_image_path, 'rb') as f:
                    new_feature.screenshot.save('project_bug.jpeg', File(f), save=False)

            new_feature.save()
            messages.success(request, 'Feature created successfully!')
            return redirect('bugs:bugs', project_id=project_id)
    
    else:
        return redirect('bugs:bugs', project_id=project_id)

def change_status(request, bug_id,project_id, status):
    user_id = request.session.get('user_id')
    if user_id:
        bug = Bug.objects.get(id=bug_id)
        bug.status = status
        bug.save()
        return redirect('bugs:bugs', project_id=project_id)
    else:
        return redirect("customuser:login")

def delete(request,project_id, bug_id):
    user_id = request.session.get("user_id")
    if user_id:
        bug = Bug.objects.get(id=bug_id)
        bug.delete()
        return redirect('bugs:bugs', project_id=project_id)
    else:
        return redirect("customuser:login")
    