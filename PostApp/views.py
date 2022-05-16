from django.shortcuts import render, get_object_or_404, redirect,HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # mixins
from .models import Post, Comment, Like  # PostApp models
from category.models import Category  # category model
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, FormView)  # class based views
from .forms import PostForm  # PostApp forms
from django.contrib.auth.models import User  # Django user model
from .forms import CommentForm
from django.core.paginator import Paginator  # pagination
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import json



def index(request):
    posts = Post.objects.order_by('-date_posted')[:4]
    context = {'posts': posts}
    return render(request, 'index.html', context)


def PostListView(request, category_slug=None):
    categories = None
    posts = None
    if category_slug != None:
        categories = get_object_or_404(Category, category_slug=category_slug)
        posts = Post.objects.filter(category=categories, is_published=True)
        posts_count = posts.count()
    else:
        posts = Post.objects.filter(is_published=True)
        posts_count = posts.count()
        paginator = Paginator(posts, 3)
        page = request.GET.get('page')
        posts = paginator.get_page(page)

    context = {
        'posts': posts,
        'posts_count': posts_count, }
    return render(request, 'posts/blog.html', context)


class UserPostListView(ListView):
    model = Post
    template_name = "posts/user_blog.html"
    context_object_name = "posts"
    paginate_by = 3

    def get_query_set(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user, is_published=True).order_by('-date_posted')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    comments = post.comments.filter(active=True)
    data= None
    is_liked = Like.objects.filter(user=user, post=post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.post = post
            data.user = user
            data.save()
            return HttpResponseRedirect('/') #hello
            
    else:
        form = CommentForm()
    
    return render(request, 'posts/blog_detail.html', {'post': post, 'is_liked': is_liked, 'form': form, 'comments': comments,'data': data})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    template_name = "posts/blog_create.html"


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    template_name = "posts/blog_create.html"


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    template_name = "posts/blog_delete.html"

# def blog(request):
#    posts=Post.objects.all()
#    context = {'posts': posts}
#    return render(request, 'posts/blog.html', context)


@login_required
def like(request):
    post_id = request.GET.get("likeId", "")
    user = request.user
    post = Post.objects.get(pk=post_id)
    liked = False
    like = Like.objects.filter(user=user, post=post)
    if like:
        like.delete()
    else:
        liked = True
        Like.objects.create(user=user, post=post)
    resp = {
        'liked': liked
    }
    response = json.dumps(resp)
    return HttpResponse(response, content_type="application/json")
