from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, User
from .forms import PostModelForm
#from django.template import loader


posts = [
    {

        'author' : 'Shravani',
        'college' : 'New York University',
        'item_type' : 'Sell',
        'cost' : '$24'
    },
    {

        'author' : 'Tanvi',
        'college' : 'New York University',
        'item_type' : 'Exchange',
        'cost' : '$10'
    },
     {

        'author' : 'Tanvi',
        'college' : 'New York University',
        'item_type' : 'Exchange',
        'cost' : '$10'
    },
]


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

    context = {
        'posts' :  posts
    }

    return render(request,'posts/home.html',context)


def profile(request):

    context = {
        'posts' :  posts
    }

    return render(request,'posts/profile.html')


