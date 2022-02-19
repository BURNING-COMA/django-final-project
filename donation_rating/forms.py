from random import choice
from turtle import title
from django import forms 

from . import models 

# RATING_OPTIONS = (
#     ('1', 'Upvote'), 
#     ('2', 'Downvote'),
#     ('3', 'No Vote'),
# )

class MakeRatingForm( forms.Form ):
    # user_rating = forms.ChoiceField(widget = forms.Select(), choices=RATING_OPTIONS, required=True)
    is_upvoted = forms.BooleanField()


class DonationForm( forms.Form):
    donate = forms.IntegerField(min_value=1)