from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostModelForm
from django.views.generic import CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

posts = [
    {
        "author": "Shravani",
        "college": "New York University",
        "item_type": "Sell",
        "cost": "$24",
    },
]

posts2 = [
    {
        "author": "Shravani",
        "college": "New York University",
        "item_type": "exchange",
        "cost": "$24",
    },
]

posts3 = [
    {
        "author": "Shravani",
        "college": "New York University",
        "item_type": "rent",
        "cost": "$24",
    },
]


# def stream_file(request, pk):
#     post = get_object_or_404(Post, id=pk)
#     response = HttpResponse()
#     response["Content-Type"] = post.content_type
#     response["Content-Length"] = len(post.picture)
#     response.write(post.picture)
#     return response


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


class postCreate(LoginRequiredMixin, CreateView):
    success_url = "/posts"
    template_name = "posts/createpost.html"
    login_url = "/accounts/login"

    def get(self, request, pk=None, post_id = None):
        
        if post_id:
            #todo add condition on edit/post_id
            post = get_object_or_404(Post, pk=post_id)
            form = PostModelForm(instance=post)
        else:
            form = PostModelForm()
        ctx = {"form": form, "post_id": post_id}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None, post_id = None):
        if post_id:
            post = get_object_or_404(Post, pk=post_id)
        else:
            post = Post()
        form = PostModelForm(request.POST, request.FILES or None, instance=post)
        # image = request.FILES.get("picture")
        # print(image)

        if not form.is_valid():
            ctx = {"form": form}
            # print("form ng")
            return render(request, self.template_name, ctx)

        # Add owner to the model before saving
        post = form.save(commit=False)
        post.user = request.user
        # ad.owner = self.request.user

        form.save()
        # form.save_m2m()
        return redirect(self.success_url)


class index(LoginRequiredMixin, View):
    login_url = "/accounts/login"

    def get(self, request):
        category = request.GET.get("category", default="all")
        option = request.GET.get("option", default="all")
        sort = request.GET.get("sort", default="all")
        post_list = Post.objects.all()
        if category != "all":
            post_list = Post.objects.filter(category=category)
        if option != "all":
            post_list = post_list.filter(option=option)
        if sort == "priceasc":
            post_list = post_list.order_by("price")
        elif sort == "pricedesc":
            post_list = post_list.order_by("-price")
        else:
            post_list = post_list.order_by("-updated_at")

        context = {"post_list": post_list}
        return render(request, "posts/home.html", context)


@login_required(login_url="/accounts/login/")
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        if 'interested' in request.POST:
            pass
        elif 'delete' in request.POST:
            post.delete()
            return redirect('posts:home')
        elif 'edit' in request.POST:
            return redirect('posts:post-edit', post_id = post_id)

    context = {"post": post, "user": request.user}
    return render(request, "posts/detail.html", context)


@login_required(login_url="/accounts/login/")
def search(request):
    q = request.GET.get("q")
    post_list = Post.objects.filter(Q(name__icontains=q))
    context = {"post_list": post_list}
    return render(request, "posts/search.html", context)
