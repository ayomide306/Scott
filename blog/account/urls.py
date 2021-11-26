from django.urls import path
from account.views import *

app_name = "account"

urlpatterns = [
        path("Login", Login, name="signin"),
        path("", Home.as_view(), name="home"),
        path("SignUp", Signup, name="signup"),
        path("Logout", Logout, name="signout"),
        path("InfoUpdate",ProfileUpdate, name="myprofile"),
        path("PasswordUpdate", ChangeMyPassword, name="passwordupdate"),
#        path("ViewOtherProfile/<int:pk>", ViewOtherProfile, name="viewotherprofile"),
]