from django.shortcuts import render,redirect,get_object_or_404 
from blog_app.forms import PostForm
from blog_app.models import Post
from django.contrib.auth.decorators import login_required 
from django.utils import timezone
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse



class PostListView(ListView):
    model=Post
    template_name="post_list.html"
    context_object_name="posts"
    
    def get_queryset(self):
        posts=Post.objects.filter(published_at__isnull=False).order_by(
            "-published_at"
        )
        return posts

    
class PostDetailView(DetailView):
    model=Post
    template_name="post_detail.html"
    context_object_name="post"

    def get_queryset(self):
        queryset=Post.objects.filter(pk=self.kwargs["pk"],published_at__isnull=False)
        return queryset
    
    
    
    

class DraftListView(LoginRequiredMixin,ListView):
    model =Post
    template_name="draft_list.html"
    context_object_name="posts"
    def get_queryset(self):
        queryset =Post.objects.filter(published_at__isnull=True)
        return queryset







class DraftDetailView(LoginRequiredMixin,DetailView):
    model=Post
    template_name="draft_detail.html"
    context_object_name="post"

    def get_queryset(self):
        queryset=Post.objects.filter(pk=self.kwargs["pk"],published_at__isnull=True)
        return queryset
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    template_name="post_create.html"
    form_class=PostForm
    
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse("draft-detail",kwargs={"pk":self.object.pk})

class PostUpdateView(LoginRequiredMixin,UpdateView):
    
    model=Post
    template_name="post_create.html"
    form_class=PostForm
    
    def get_success_url(self):
        post=self.get_object()
        if post.published_at:
            return reverse("post-detail",kwargs={"pk":post.pk})
        else:
            return reverse("draft-detail",kwargs={"pk":post.pk})

    
    
class PostDeleteView(LoginRequiredMixin,View):
    def get(self,request,pk):
        post =Post.objects.get(pk=pk)
        post.delete()
        if post.published_at:
         return redirect("post-list")
        else:
         return redirect("post-draft")   
    

    




class DraftPublishView(LoginRequiredMixin,View):
    def get(self,request,pk):
        post=Post.objects.get(pk=pk,published_at__isnull=True)
        post.published_at=timezone.now()
        post.save()
        return redirect ("post-list")


    