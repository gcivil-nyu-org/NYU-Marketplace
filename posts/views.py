from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostModelForm
from django.views.generic import CreateView, View
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

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


class postCreate(LoginRequiredMixin, CreateView):
    success_url = '/posts'
    template_name = "posts/createpost.html"
    login_url = '/accounts/login'

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


class index(LoginRequiredMixin, View):
    login_url = '/accounts/login'

    def get(self, request):
        category = request.GET.get('category', default='all')
        option = request.GET.get('option', default='all')
        sort = request.GET.get('sort', default='all')
        post_list = Post.objects.all()
        if category != 'all':
            post_list = Post.objects.filter(category = category)
        if option != 'all':
            post_list =post_list.filter(option = option)
        if sort == 'pricedesc':
            post_list.order_by('price').desc()
        elif sort == 'priceasc':
            post_list.order_by('price').asc()
        else:
            post_list.order_by('-updated_at')

        context = {
            'post_list': post_list
        }
        return render(request, 'posts/home.html', context)



@login_required(login_url='/accounts/login/')
def profile(request):

    context = {
        'posts' :  posts
    }

    return render(request,'posts/profile.html')


@login_required(login_url='/accounts/login/')
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    # try:
    #     selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'polls/detail.html', {
    #         'question': question,
    #         'error_message': "You didn't select a choice.",
    #     })
    # else:
    #     #selected_choice.votes += 1
    #     #selected_choice.save()
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.
    context={
        'post' : post
    }
    return render(request, 'posts/detail.html', context)