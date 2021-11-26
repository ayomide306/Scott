from dashboard.form import *
from datetime import timezone
from post.models import Posts
from django.http import HttpResponse
from django.db.models import Q
from newsletter.models import Newsletter
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
"""
    Search Function
"""
def Search(request):
    query = request.GET.get('query')
    result = Posts.objects.filter(
        Q(title__icontains=query) 
          | Q(sub__icontains=query) 
          | Q(content__icontains=query)
    )
    context = {
        "results":result
    }
    return render(request, "Posts/Search.htm", context)
"""
    Function For Creating New Post
"""
def CreatePost(request):
    if request.user.is_superuser:
        form = PostForm()
        if request.method == "POST" or request.method == "FILES":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                forms = form.save(commit=False)
                forms.author = request.user
                forms.save()
                context = {
                    "form":form,
                    "success":"Post Created Successfully"
                }
                return render(request, "Dashboard/CreatePost.htm", context)
            else:
                context = {
                    "form":form,
                    "error":"Post Not Created"
                }
                return render(request, "Dashboard/CreatePost.htm", context)
        context = {
            "form":form
        }
        return render(request, "Dashboard/CreatePost.htm", context)
"""
    Delete Post
"""
def DeletePost(request, pk):
    if request.user.is_superuser:
        post = get_object_or_404(Posts, pk=pk)
        if request.method == "POST":
            post.delete()
            return HttpResponse('deleted')
        else:
            context = {
                'post':post
            }
            return render(request, 'Dashboard/DeletePost.htm', context)
"""
    Editing Post
"""
def EditPost(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    if request.method == "POST" or request.method == "FILES":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            context = {
                 "form":form,
                 "success":"Post Updated Successfully"
            }
            return render(request, "Dashboard/EditPost.htm", context)
        else:
            form = PostForm(instance=post)
            context = {
                "form":form,
                "error":"Sorry Post Was Not Edited Successful"
            }
            return render(request, "Dashboard/EditPost.htm", context)
    else:
        form = PostForm(instance=post)
        context = {
            "form":form
        }
        return render(request, "Dashboard/EditPost.htm", context)
"""
    Main Dashboard Page Fixture    
"""
def Dashboard(request):
    if request.user.is_superuser:
        users = User.objects.order_by("-pk").exclude(username=request.user.username)
        posts = Posts.objects.order_by("-like")
        posthate = Posts.objects.order_by("-hate")
        postheart = Posts.objects.order_by("-love")
        postlike = Posts.objects.order_by("-like")
        #postview = Posts.objects.values_list("view").order_by("-view").distinct()
        comm = Posts.objects.order_by("commentss")
        news = Newsletter.objects.order_by("-pk")
        postpk = Posts.objects.order_by("-pk")
        context = {
            "news":news,
            "users":users,
            "posts":posts,
            "postpk":postpk,
            "postcomment":comm,
            "posthate":posthate,
            "postlike":postlike,
           # "postview":postview,
            "postheart":postheart
        }
        return render(request, "Dashboard/Dashboard.htm", context)


