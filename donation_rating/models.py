from operator import mod
from pyexpat import model
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User 
from django.db import models
from users.models import Profile
# Create your models here.


# class Category(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=50)

class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    # title = models.CharField(max_length=50)
    # details = models.TextField()
    
    # start_date = models.DateField()
    #  # general_rate = models.IntegerField(default=0)    # FIXME AA
     
    end_date = models.DateField()
    total_target = models.IntegerField(default=0, null=True, blank=True)
    total_upvotes = models.IntegerField(default=0,null=True, blank=True)  # FIXME AA
    total_votes = models.IntegerField(default=0, null=True,blank=True)    # FIXME AA
    collected_donations = models.IntegerField(default=0,null=True, blank=True) # FIXME AA
    is_deleted = models.BooleanField(default=False,blank=True)

    # category = models.ForeignKey(Category,on_delete=models.CASCADE)
    # tags = models.ManyToManyField('Tags')
    # photo = models.ManyToManyField('Images')

    # TODO link to Profile instead of User
    user = models.ForeignKey(User,on_delete=models.CASCADE) # AA
    # photo = models.ForeignKey('ProjectImages',on_delete=models.CASCADE,null=True)



# FIXME AA
class ProjectRate(models.Model):
    id = models.AutoField(primary_key=True)
    # TODO link to Profile instead of User
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    is_upvote = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)



# class Tags(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=50)


# class ProjectImages(models.Model):
#     id = models.AutoField(primary_key=True)
#     project = models.ForeignKey(Projects, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='projects/')