from django.urls import path
from post.views import *

app_name = 'post'

urlpatterns = [
    path('Comment', Comments, name='comment'),
    path('LikePost', LikePost, name='likepost'),
    path('HatePost', HatePost, name='hatepost'),
    path('LovePost', LovePost, name='lovepost'),
    path('EditReply/<int:pk>', EditReply, name='editreply'),
    path("Reply/<int:pk>", ReplyComment, name='replycomment'),
    path('EditComment/<int:pk>', EditComment, name='editcomment'),
    path('DeleteReply/<int:pk>', DeleteReply, name='deletereply'),
    path('Viewing/<int:pk>/<str:name>', ViewPost, name='viewpost'),
    path('DeleteComment/<int:pk>', DeleteComment, name='deletecomment'),
]
