from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Post, Group
from .forms import PostForm


def index(request):
    latest = Post.objects.order_by("-pub_date")[:11]
    return render(request, "posts/index.html", {"posts": latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by("-pub_date")[:12]
    return render(request, "posts/group.html", {"group": group, "posts": posts}) 


def new_post(request):
    user = request.user
    form = PostForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            n_post = form.save(commit=False)
            n_post.author = user
            n_post.save()
            return redirect('index')
        return render(request, 'posts/new_post.html', {'form': form})        
    form = PostForm()
    return render(request, 'posts/new_post.html', {'form': form})   
    