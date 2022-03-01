from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostModelForm
from django.template import loader


def post_create(request):
    form = PostModelForm()
    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/posts')
    context = {
        "form": form
    }
    return render(request, "posts/createpost.html", context)


def index(request):
    latest_posts_list = Post.objects.order_by('-updated_at')[:5]
    template = loader.get_template('posts/home.html')
    context = {
        'posts': latest_posts_list,
    }
    return HttpResponse(template.render(context, request))


def profile(request):

    # context = {
    #     'posts' :  posts
    # }

    return render(request,'posts/profile.html')


