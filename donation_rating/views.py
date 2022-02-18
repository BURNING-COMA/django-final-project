from http.client import HTTPResponse
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required

from . import models
# Create your views here.


@login_required(login_url='login')
def home(request, project_id):
    # user_id = request.user.profile.user_id
    # return render(request, 'donation_rating/home.html',
    #      {'user_id':user_id, 'project_id': project_id})
    
    project = models.Projects.objects.get( id = project_id )
    # Workaround to avoid making custom tag/filter for subtraction 
    total_downvotes = project.total_votes - project.total_upvotes
    remaining_sum = project.total_target - project.collected_donations
    return render(request, 'donation_rating/home.html', {'project':project, 
        'total_downvotes' : total_downvotes, 
        'remaining_sum' : remaining_sum
        })
