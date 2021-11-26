from django.http import HttpResponse
from django.views.generic import ListView
from post.models import Posts, Comment, Reply
from post.form import CommentEditForm, ReplyEditForm
from django.shortcuts import get_object_or_404, render, redirect
"""
    Deleting A Reply By Logined In User
"""
def DeleteReply(request, pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Reply, pk=pk)
        #post = comment.post
        if request.method == "POST":
            comment.delete()
            return HttpResponse("deleted")
        else:
            context = {
                "comment":comment
            }
            return render(request, "Posts/Reply.htm", context)
    else:
        return HttpResponse("Sorry Why Trying This")
        return redirect("/")

"""
    Editing A Reply By Logined In User
"""
def EditReply(request, pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Reply, pk=pk)
        if request.user.username == comment.user.username:
            if request.method == "POST":
                form = ReplyEditForm(request.POST ,instance=comment)
                if form.is_valid():
                    form.save()
                    return ViewPost(request, pk=comment.comments.post.pk, name=comment.comments.post.title)
                    #return redirect("viewpost", pk=comment.comments.post.pk, name=comment.comments.post.title)
            else:
                commentform = ReplyEditForm(instance=comment)
                context = {
                    "commentform":commentform
                }
                return render(request, "Posts/ReplyEdit.htm", context)

"""
    Reply To Comment
"""
def ReplyComment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    replies = Reply.objects.filter(comments=comment).order_by("-pk")
    if request.user.is_authenticated:
        if request.method == "POST":
           reply = request.POST.get("replies")
           print(reply)
           username = request.user
           replying = Reply(comments=comment, user=username,said=reply)
           replying.save()
           repliess = Reply.objects.filter(comments=comment)
           for replys in repliess:
               comment.rply.add(replys) 
           return HttpResponse("saved")
        else:
            context = {
                "comment":comment,
                "replies":replies
            }
            return render(request, "Posts/Replying.htm", context)
    else:
        return redirect("/")

"""
    Deleting A Comment By Logined In User
"""
def DeleteComment(request, pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=pk)
        post = comment.post
        if request.method == "POST":
            comment.delete()
            return HttpResponse("deleted")
        else:
            context = {
                "comment":comment
            }
            return render(request, "Posts/Comment.htm", context)
    else:
        return HttpResponse("Sorry Why Trying This")
        return redirect("/")

"""
    Editing A Comment By Logined In User
"""
def EditComment(request, pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=pk)
        if request.user.username == comment.user:
            if request.method == "POST":
                form = CommentEditForm(request.POST ,instance=comment)
                if form.is_valid():
                    form.save()
                    return ViewPost(request, pk=comment.post.pk, name=comment.post.title)
            else:
                commentform = CommentEditForm(instance=comment)
                context = {
                    "commentform":commentform
                }
                return render(request, "Posts/CommentEdit.htm", context)
"""
        Commenting on A Post
"""
def Comments(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            postes = request.POST.get("postid")
            posts = get_object_or_404(Posts, pk=postes)
            username = request.user.username
            said = request.POST.get("said")
            #emails = get_object_or_404(User, pk=request.user.pk)
            #email = request.user.email
            comments = Comment(post=posts, user=username,said=said)
            comments.save()
            commenting = Comment.objects.filter(post=posts)
            for comment in commenting:
                posts.commentss.add(comment)
                
            #posts.commentss = 
            return HttpResponse("saved")      
    else:
        postes = request.POST.get("postid")
        posts = get_object_or_404(Posts, pk=postes)
        username = request.POST.get("username")
        said = request.POST.get("said")
        #emails = get_object_or_404(User, pk=request.user.pk)
        #email = request.user.email
        comments = Comment(post=posts, user=username,said=said)
        comments.save()
        commenting = Comment.objects.filter(post=posts)
        for comment in commenting:
            posts.commentss.add(comment)
            
        #posts.commentss = 
        return HttpResponse("saved")      
"""
        Like Post
"""
def LikePost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            postes = request.POST.get('postid')
            post = get_object_or_404(Posts, pk=postes)
            ip = request.user.id
            if post.like.filter(id=ip):
                post.like.remove(ip)
            else:
                post.like.add(ip)
            if post.hate.filter(id=ip):
                post.hate.remove(ip)
            if post.love.filter(id=ip):
                post.love.remove(ip)
            return HttpResponse('allowed')
    else:
        return HttpResponse('unallowed')
        return redirect("/")
            

"""
        Dislike Blog Post 
"""
def HatePost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            postes = request.POST.get('postid')
            post = get_object_or_404(Posts, pk=postes)
            ip = request.user.id
            if post.hate.filter(id=ip):
                post.hate.remove(ip)
            else:
                post.hate.add(ip)
            if post.like.filter(id=ip):
                post.like.remove(ip)
            if post.love.filter(id=ip):
                post.love.remove(ip)
            return HttpResponse('allowed')
    return HttpResponse('unallowed')
    return redirect("/")
"""
        Heart Blog Post
"""
def LovePost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            postes = request.POST.get('postid')
            post = get_object_or_404(Posts, pk=postes)
            ip = request.user.id
            if post.love.filter(id=ip):
                post.love.remove(ip)
            else:
                post.love.add(ip)
            if post.like.filter(id=ip):
                post.like.remove(ip)
            if post.hate.filter(id=ip):
                post.hate.remove(ip)
            return HttpResponse('allowed')
    return HttpResponse('unallowed')
    return redirect("/")
"""
        Viewing A blog post with the id(pk)
"""
def ViewPost(request, pk, name):
    post = get_object_or_404(Posts, pk=pk)
    comment = Comment.objects.filter(post=post)
    latestpost = Posts.objects.all().order_by("-pk")[0:3]
    for comments in comment:
        post.commentss.add(comments)
    ip = request.user.id
    liked = False
    hated = False
    loved = False
    context = {
            'postviews':post,
            'comment':comment,
            "latestpost":latestpost
        }
    if request.user.is_authenticated:
        if post.like.filter(id=ip):
            liked = True
        if post.hate.filter(id=ip):
            hated = True
        if post.love.filter(id=ip):
            loved = True
        if post.view.filter(id=ip):
            context = {
                'postviews':post,
                'liked':liked,
                'hated':hated,
                'loved':loved,
                'comment':comment,
                "latestpost":latestpost
            }
            return render(request, 'Posts/PostView.htm', context)
        else:
            post.view.add(ip)
            context = {
                'postviews':post,
                'liked':liked,
                'hated':hated,
                'loved':loved,
                'comment':comment,
                "latestpost":latestpost
            }
            return render(request, 'Posts/PostView.htm', context)
    return render(request, 'Posts/PostView.htm', context)
    #return redirect("/")

    
    

