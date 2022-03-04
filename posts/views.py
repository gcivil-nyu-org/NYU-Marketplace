from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostModelForm
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
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


def stream_file(request, pk):
    post = get_object_or_404(Post, id=pk)
    response = HttpResponse()
    response['Content-Type'] = post.content_type
    response['Content-Length'] = len(post.picture)
    response.write(post.picture)
    return response


# def post_create(request):
#     form = PostModelForm()
#     if request.method == "POST":
#         form = PostModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/posts')
#     context = {
#         "form": form
#     }
#     return render(request, "posts/createpost.html", context)


class postCreate(CreateView):
    success_url = '/posts'
    template_name = "posts/createpost.html"

    def get(self, request, pk=None):
        form = PostModelForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = PostModelForm(request.POST, request.FILES or None)
        image = request.FILES.get('picture')
        print(image)

        if not form.is_valid():
            ctx = {'form': form}
            print("form ng")
            return render(request, self.template_name, ctx)

        # Add owner to the model before saving
        #post = form.save(commit=False)
        #ad.owner = self.request.user
        form.save()
        #form.save_m2m()
        return redirect(self.success_url)


def index(request):
    post_list = Post.objects.all().order_by('-updated_at')[:10]
    context = {
        'post_list' :  post_list
    }

    return render(request,'posts/home.html',context)


def profile(request):

    context = {
        'posts' :  posts
    }

    return render(request,'posts/profile.html')