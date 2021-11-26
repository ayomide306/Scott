from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
#Create a profile instance for all newly registered users
class Profile(models.Model):
     user = models.OneToOneField(User,   on_delete = models.CASCADE)
     profilepic = models.FileField(upload_to = "Profile/ProfilePic/", default = "Profile/User.jpg")
     phone = models.IntegerField(blank = True, null =True)
     bio = models.TextField(default = "Little About Me")
     @receiver(post_save, sender = User)
     def create_user_profile(sender, instance, created, **kwargs):
          if created:
              
               Profile.objects.create(user = instance)
     
     @receiver(post_save, sender = User)
     def save_user_profile(sender, instance, **kwargs):
          instance.profile.save()
          
     def __str__(self):
         return self.user.username





