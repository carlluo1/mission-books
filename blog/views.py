from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from .forms import AdminForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

@login_required
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def process(request):
    return render(request, 'registration/process.php', {})

@login_required
def title_page(request):
    #post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/title_page.html', {})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def sign_up(request):
    if request.method == "POST":
        form = AdminForm(request.POST)
        if form.is_valid():
            admin = form.save(commit=False)
            admin.save()
            return redirect('login')
    else:
        form = AdminForm()
    return render(request, 'registration/sign_up.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

