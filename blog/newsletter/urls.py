from django.urls import path
from newsletter.views import *

app_name = 'newsletter'

urlpatterns = [
    path("JoinLetter", JoinLetter),
    path("LeaveLetter", LeaveLetter),
    path("SendingNewsletter", SendLetter),
]
