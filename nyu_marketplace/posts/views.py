from django.shortcuts import render
from django.http import HttpResponse
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


def createpost(request):

    context = {
        'posts' :  posts
    }

    
    return render(request,'posts/createpost.html')

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


