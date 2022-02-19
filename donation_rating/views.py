from http.client import HTTPResponse
from operator import mod
from pyexpat import model
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required

from . import models
from . import forms 
# Create your views here.

def update_rating(request, project_id):
    user_id = request.user.id
    if request.method == 'POST':
        ratingForm = forms.MakeRatingForm(request.POST)
        if ratingForm.is_valid():
            did_upvote = ratingForm.cleaned_data["is_upvoted"]
            # depending on current user voting and new voting, update 
            # project: total voting, total upvotes 
            # projectRating: is_vote, remove or add from table 
            user_has_upvoted = models.ProjectRate.objects.filter( user = user_id).exists()
            if not user_has_upvoted and did_upvote:
                models.ProjectRate.objects.create(is_upvote=True, user=request.user, project=models.Projects.objects.get(id=project_id))
                cur_project = models.Projects.objects.get(id=project_id)
                cur_project.total_upvotes += 1
                cur_project.total_votes += 1
                cur_project.save()
            return redirect(f'/do_ra/project/{project_id}')
    return HttpResponse('invalid')


@login_required(login_url='login')
def home(request, project_id):
    # TODO change user_id = request.user.profile.user_id
    user_id = request.user.id
    # return render(request, 'donation_rating/home.html',
    #      {'user_id':user_id, 'project_id': project_id})
    
    project = models.Projects.objects.get( id = project_id )
    # Workaround to avoid making custom tag/filter for subtraction 
    total_downvotes = project.total_votes - project.total_upvotes
    remaining_sum = project.total_target - project.collected_donations

    #determine user feedback 
    # precondition: there is at most one record in projectRating for any user
    # post: cur_user_feed_msg has a matching value with 
    # does the record exist ?

    # determine current user rate for the project. did he make a rate ? what is it ?
    user_has_rate = models.ProjectRate.objects.filter( user = user_id).exists()
    if user_has_rate: 
        cur_user_rate =  models.ProjectRate.objects.get( user = user_id )

    # message that show user his current rate
    cur_user_rate_msg = 'You did not vote for this project'
    if user_has_rate: 
        if cur_user_rate.is_upvote:
            cur_user_rate_msg = 'You upvoted this project'
        else: 
            # the feature of downvote will be added later.
            cur_user_rate_msg = 'You downvoted this project'


    ratingForm = forms.MakeRatingForm()

    return render(request, 'donation_rating/home.html', {'project':project, 
        'total_downvotes' : total_downvotes, 
        'remaining_sum' : remaining_sum, 
        'cur_user_rate_msg' : cur_user_rate_msg,
        'ratingForm' : ratingForm,
        'project_id' : project_id,
        })
