from django import forms
from post.models import Posts 
"""
    Creating Post
"""
class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ("title","image","sub","content",)
"""
    Creating Post
"""
