from django import forms
from post.models import Comment, Reply, Posts
"""
    Form for Editing Comment
"""
class CommentEditForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('said',)

"""
    Form for Editing Reply
"""
class ReplyEditForm(forms.ModelForm):
    
    class Meta:
        model = Reply
        fields = ('said',)
"""

"""

"""

"""
