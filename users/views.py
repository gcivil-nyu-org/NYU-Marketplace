from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile
from posts.models import Post

# @login_required(login_url="/accounts/login/")
# def profile(request):
#     # if request.method == "POST":
#     #     # profile = Profile.objects.create(user=request.user)
#     #     # form = ProfileForm(request.POST, instance=profile)
#     #     # form.save()
#     #     # return redirect("posts:home")
#     #     # print(hi)
#     # else:
#     form = ProfileForm()
#     return render(request, "users/profile.html", {"form": form})


@login_required(login_url="/accounts/login/")
def profile_detail(request):
    posts = Post.objects.all()
    posts = posts.filter(user=request.user)
    user_info = Profile.objects.get(user=request.user)
    # user_info = user_info.filter(user=request.user)

    context = {"post_list": posts, "user": user_info, "default_user": request.user}
    return render(request, "users/profile_detail.html", context)


@login_required(login_url="/accounts/login/")
def user_info(request, user_id):
    posts = Post.objects.all()
    posts = posts.filter(user=user_id)
    user_info = Profile.objects.get(user=user_id)
    context = {"post_list": posts, "user": user_info, "default_user": request.user}
    if request.user.id == user_id:
        return render(request, "users/profile_detail.html", context)
    return render(request, "users/user_info.html", context)


@login_required(login_url="/accounts/login/")
def edit_profile(request):

    if request.method == "POST":
        form = ProfileForm(
            request.POST, request.FILES or None, instance=request.user.profile
        )
        if not form.is_valid():
            ctx = {"form": form}
            return render(request, "users/edit_profile.html", ctx)
        form.save()
        return redirect("posts:home")
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, "users/edit_profile.html", {"form": form})
