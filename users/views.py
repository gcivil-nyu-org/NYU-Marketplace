from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileForm
from .models import Profile

from posts.models import Post, Report, Interest

# from notifications.models import notification
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User

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
    user_account = User.objects.get(id=user_id)
    if len(Interest.objects.filter(interested_user=request.user)) > 0:
        user_interested_list = []
        list = Interest.objects.filter(interested_user=request.user).values_list("post")
        for item in list:
            user_interested_list.append(item[0])
    else:
        user_interested_list = []
    context = {
        "post_list": posts,
        "user": user_info,
        "default_user": request.user,
        "user_account": user_account,
        "user_interested_list": user_interested_list,
    }
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
        return redirect("users:profile_detail")
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, "users/edit_profile.html", {"form": form})


@login_required(login_url="/accounts/login/")
def post_interest_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    interest_list = None
    report_list = None

    if request.method == "POST":
        if (
            post.user == request.user or request.user.is_superuser
        ) and "delete" in request.POST:
            post.delete()
            return redirect("posts:home")
        elif post.user == request.user and "edit" in request.POST:
            return redirect("posts:post-edit", post_id=post_id)
        else:
            raise PermissionDenied()
    else:
        if request.user == post.user:
            interest_list = Interest.objects.filter(post=post)
        elif request.user.is_superuser:
            report_list = Report.objects.filter(post=post)
        else:
            raise PermissionDenied

    context = {
        "post": post,
        "user": request.user,
        "interest_list": interest_list,
        "report_list": report_list,
    }
    return render(request, "users/post_interest_detail.html", context)


def about_us(request):

    return render(request, "users/about_us.html")


# @login_required(login_url="/accounts/login/")
# def mark_all_as_read(request):
#     posts.filter(user=request.user)
#     return
