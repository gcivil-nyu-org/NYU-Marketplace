from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile
from posts.models import Post

# Create your views here.
# def userTest(request):
#    return HttpResponse("Hello, world. You're at the polls index.")


@login_required(login_url="/accounts/login/")
def profile(request):
    if request.method == "POST":
        profile = Profile.objects.create(user=request.user)
        form = ProfileForm(request.POST, instance=profile)
        form.save()
        return redirect("posts:home")
    else:
        form = ProfileForm()
    return render(request, "users/profile.html", {"form": form})


@login_required(login_url="/accounts/login/")
def profile_detail(request):
    posts = Post.objects.all()
    posts = posts.filter(user=request.user)
    user_info = Profile.objects.get(user=request.user)
    # user_info = user_info.filter(user=request.user)

    context = {
        "post_list": posts,
        "user": user_info,
        "default_user": request.user
    }
    return render(request, "users/profile_detail.html", context)
