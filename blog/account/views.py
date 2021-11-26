from post.models import *
from account.form import *
from account.models import *
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
"""
    Changing Password
"""
def ChangeMyPassword(request):
    if not request.method == "POST":
        form = PasswordChangeForm(request.user)
        context = {
            "form":form
        }
        return render(request, "Account/PasswordChange.htm", context)
    else:
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = PasswordChangeForm(request.user)
            context = {
                "form":form,
                "error":"Sorry An Error Ocurred, Try Again Please"
            }
            return render(request, "Account/PasswordChange.htm", context)
"""
    Updating My Profile Page 
"""
def ProfileUpdate(request):
    if request.method == "POST" or request.method == "FILES":
        userform = UserForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST, request.FILES,instance=request.user.profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            userform = UserForm(instance=request.user)
            profileform = ProfileForm(instance=request.user.profile)
            context = {
                "profileform":profileform,
                "userform":userform,
                "worked":"Info Updated Successful"
            }
            return render(request, "Account/ProfileUpdate.htm", context)
        else:
            userform = UserForm(instance=request.user)
            profileform = ProfileForm(instance=request.user.profile)
            context = {
                "profileform":profileform,
                "userform":userform,
                "worked":"Sorry Info Updated Was Not Successful. Pls Try Again Later"
            }
            return render(request, "Account/ProfileUpdate.htm", context)
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=request.user.profile)
        context = {
            "profileform":profileform,
            "userform":userform
        }
        return render(request, "Account/ProfileUpdate.htm", context)
"""
    Profile Page(For Viewing Personal Profile and Other Profile)
"""
"""
def ViewOtherProfile(request, pk):
    user = get_object_or_404(User, pk=pk)
    context = {
        "otherprofile":user
    }
    return render(request, "Profile/ViewOtherProfile.htm", context)

def ViewMyProfile(request):
    return render(request, "Profile/MyProfile.htm")
"""
"""
        Defining the Home Page View
"""
class Home(ListView):
    model = Posts
    queryset =  Posts.objects.all()
    context_object_name = 'posts'
    template_name='Posts.htm'
    paginate_by = 15
"""
       Logout View 
"""
def Logout(request):
    logout(request)
    return redirect("/")

"""
        Login Already Registered users with their username
"""
def Login(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            username = request.POST.get("uname")
            password = request.POST.get("pwrd")
            
            user = authenticate(request, username=username, password=password)
            
            if user is None:
                error = "Invalid Credatials Provided"
                context = {
                    "loginerror":error
                }
                return render(request, "Account/Register.htm",context)
            else:
                login(request, user)
                return redirect("/")
                
                
"""
        Registering a new user with custom html
"""
def Signup(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "GET":
            return render(request, "Account/Register.htm")
        else:
            username = request.POST.get("uname")
            email = request.POST.get("email")
            password = request.POST.get("pwrd")
          #  cpassword = request.POST.get("cpassword")
            if User.objects.filter(username=username).exists():
                users = "Username is Taken"
                context = {
                        "error":users
                }
                return render(request, "Account/Register.htm", context)
            elif User.objects.filter(email=email).exists():
                users = "Email is taken"
                context = {
                        "error":users
                }
                #return HttpResponse(users)
                return render(request, "Account/Register.htm", context)
            else:
                user = User.objects.create_user(username,
                    email,
                    password
                    )
                user.save()
                login(request, user)
                return redirect("/")

