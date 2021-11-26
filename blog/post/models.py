import datetime
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

class Reply(models.Model):
    comments = models.ForeignKey("Comment",on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    said = models.TextField()
    saon = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(User, blank=True ,related_name="replylike")
    hate = models.ManyToManyField(User, blank=True, related_name="replyhate")
    love = models.ManyToManyField(User, blank=True ,related_name="replylove")

    
    def __str__(self):
        return self.user.username

class Comment(models.Model):
    post = models.ForeignKey("Posts", on_delete=models.CASCADE)
    user = models.CharField(max_length=250)
    said = models.TextField()
    saon = models.DateTimeField(auto_now_add=True)
    rply = models.ManyToManyField(Reply, blank=True, null=True ,related_name="replys")
    like = models.ManyToManyField(User, blank=True,related_name="commentlike")
    hate = models.ManyToManyField(User, blank=True,related_name="commenthate")
    love = models.ManyToManyField(User, blank=True, related_name="commentlove")
    def __str__(self):
        return self.user
    class Meta:
        ordering = ["-saon"]


class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to="Post/Pic")
    title = models.CharField(max_length=250)
    sub = models.CharField(max_length=255, blank=True)
    content = RichTextUploadingField()
    commentss = models.ManyToManyField(Comment, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    view = models.ManyToManyField(User, blank=True, related_name='view')
    like = models.ManyToManyField(User, blank=True ,related_name="like")
    hate = models.ManyToManyField(User, blank=True ,related_name="hate")
    love = models.ManyToManyField(User, blank=True ,related_name="love")
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-pk"]
    