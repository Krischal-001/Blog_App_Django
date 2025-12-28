from django.shortcuts import render,redirect,get_object_or_404 
from blog_app.forms import PostForm
from blog_app.models import Post
from django.contrib.auth.decorators import login_required 
from django.utils import timezone


def post_list(request):
    posts=Post.objects.filter(published_at__isnull=False)
    return render(
        request,
        "post_list.html",
        {"posts":posts}
    )
    
def post_detail(request,pk):
    post=Post.objects.get(pk=pk)
    return render(
        request,
        "post_detail.html",
        {"post":post}
    )
@login_required
def post_draft(request):
    
    posts=Post.objects.filter(published_at__isnull=True)
    return render(
        request,
        "draft_list.html",
        {"posts":posts}
    )
@login_required
def draft_detail(request,pk):
    post=Post.objects.get(pk=pk,published_at__isnull=True)
    return render(
        request,
        "draft_detail.html",
        {"post":post}
    )
def post_create(request):
    if request.method == "GET":
     form=PostForm()
     return render(
         request,
         "post_create.html",
         {"form":form}
     )
    else :
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect("draft-detail",pk=post.pk)
        else:
            return render(
                request,
                "post_create.html",
                {"form":form}
            ) 

@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            if post.published_at:
                return redirect("post-detail", post.pk)
            else:
                return redirect("draft-detail", post.pk)
    else:
        form = PostForm(instance=post)

    return render(
        request,
        "post_create.html",
        {"form": form}
    )
@login_required
def post_delete(request, pk):
    post =Post.objects.get(pk=pk)
    post.delete()
    if post.published_at:
        return redirect("post-list")
    else:
        return redirect("post-draft")
    
@login_required
def draft_publish(request,pk):
    post=Post.objects.get(pk=pk,published_at__isnull=True)
    post.published_at=timezone.now()
    post.save()
    return redirect ("post-list")