from random import choice
from turtle import title
from django import forms 

from . import models 


# TODO add downvote
# RATING_OPTIONS = (
#     ('1', 'Upvote'), 
#     ('2', 'Downvote'),
#     ('3', 'No Vote'),
# )

class MakeRatingForm( forms.Form ):
    # user_rating = forms.ChoiceField(widget = forms.Select(), choices=RATING_OPTIONS, required=True)
    CHOICES=[('upvote','Upvote'),
         ('no_upvote','No Upvote')]
    voting = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)


class DonationForm( forms.Form):
    donate = forms.IntegerField(min_value=1)