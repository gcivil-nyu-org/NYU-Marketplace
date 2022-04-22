from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Report, Interest, User
from .forms import PostModelForm
from django.views.generic import CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.core.exceptions import PermissionDenied
from notifications.signals import notify


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

    def get(self, request, pk=None, post_id=None):
        if request.user.is_superuser:
            raise PermissionDenied()
        if post_id:
            post = get_object_or_404(Post, pk=post_id)
            if post.user != request.user:
                raise PermissionDenied()
            form = PostModelForm(instance=post)
        else:
            form = PostModelForm()
        ctx = {"form": form, "post_id": post_id}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None, post_id=None):
        if request.user.is_superuser:
            raise PermissionDenied()
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
        q = request.GET.get("q", default="")
        post_list = Post.objects.all()
        post_list_pk = Post.objects.all().values("pk")
        if len(Interest.objects.filter(interested_user=request.user)) > 0:
            user_interested_list = Interest.objects.filter(
                interested_user=request.user
            ).values_list("post")[0]
        else:
            user_interested_list = ()
            # print(user_interested_list)
        if q != "":
            post_list = post_list.filter(Q(name__icontains=q))
        if category != "all":
            post_list = post_list.filter(category=category)
        if option != "all":
            if option == "reported":
                if request.user.is_superuser:
                    post_list = post_list.filter(report_count__gte=1)
                    post_list = post_list.order_by("-report_count")
                else:
                    raise PermissionDenied()
            else:
                post_list = post_list.filter(option=option)
        if sort == "priceasc":
            post_list = post_list.order_by("price")
        elif sort == "pricedesc":
            post_list = post_list.order_by("-price")
        elif option != "reported":
            post_list = post_list.order_by("-created_at")
        context = {
            "post_list": post_list,
            "user": request.user,
            "user_interested_list": user_interested_list,
            "post_list_pk": post_list_pk,
        }
        # print(post_list_pk)
        # print(user_interested_list)
        return render(request, "posts/home.html", context)


# TODO do if else both cleaner - both here and in detail.html


@login_required(login_url="/accounts/login/")
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    interest_list = None
    report_list = None
    admin_check_report = False
    is_reported_by_user = False
    is_user_already_interested = False
    if Report.objects.filter(post=post):
        admin_check_report = True
    if Report.objects.filter(reported_by=request.user, post=post):
        is_reported_by_user = True
    if Interest.objects.filter(interested_user=request.user, post=post):
        is_user_already_interested = True

    if request.method == "POST":
        if (
            post.user != request.user
            and "interested" in request.POST
            and not is_user_already_interested
        ):
            cust_message = request.POST.get("cust_message")
            post.interested_count += 1
            post.save()
            interest = Interest(
                interested_user=request.user, post=post, cust_message=cust_message
            )
            interest.save()
            sender = User.objects.get(username=request.user)
            receiver = User.objects.get(username=post.user)
            notify.send(
                sender,
                recipient=receiver,
                verb="",
                description=sender.username
                + " is interested in your post "
                + post.name,
            )
            is_user_already_interested = True
            context = {
                "post": post,
                "user": request.user,
                "is_reported_by_user": is_reported_by_user,
                "is_user_already_interested": is_user_already_interested,
                "interest_list": interest_list,
            }
            return render(request, "posts/detail.html", context)
            # return redirect("posts:home")
        elif (
            post.user != request.user
            and "cancel_interest" in request.POST
            and is_user_already_interested
        ):
            post.interested_count -= 1
            post.save()
            interest = Interest.objects.filter(interested_user=request.user, post=post)
            interest.delete()
            is_user_already_interested = False
            context = {
                "post": post,
                "user": request.user,
                "is_reported_by_user": is_reported_by_user,
                "is_user_already_interested": is_user_already_interested,
                "interest_list": interest_list,
            }
            return render(request, "posts/detail.html", context)
            # return redirect("posts:home")
        elif (
            post.user != request.user
            and "report" in request.POST
            and not is_reported_by_user
        ):
            post.report_count += 1
            post.save()
            # print(request.POST.get("report_option"))
            # report = Report(reported_by=request.user, post=post, reasons=request.POST.get("report_option"))
            report = Report(
                reported_by=request.user,
                post=post,
                reason=request.POST.get("report_option"),
            )
            report.save()
            is_reported_by_user = True
            context = {
                "post": post,
                "user": request.user,
                "is_reported_by_user": is_reported_by_user,
                "is_user_already_interested": is_user_already_interested,
                "interest_list": interest_list,
            }
            return render(request, "posts/detail.html", context)
            # return redirect("posts:home")
        elif (
            post.user != request.user
            and "cancel_report" in request.POST
            and is_reported_by_user
        ):
            post.report_count -= 1
            post.save()
            report = Report.objects.filter(reported_by=request.user, post=post)
            report.delete()
            is_reported_by_user = False
            context = {
                "post": post,
                "user": request.user,
                "is_reported_by_user": is_reported_by_user,
                "is_user_already_interested": is_user_already_interested,
                "interest_list": interest_list,
            }
            return render(request, "posts/detail.html", context)
            # return redirect("posts:home")
        elif (
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
        if request.user.is_superuser:
            if admin_check_report:
                report_list = Report.objects.filter(post=post)
                # print(report.reason)

    context = {
        "post": post,
        "user": request.user,
        "is_reported_by_user": is_reported_by_user,
        "is_user_already_interested": is_user_already_interested,
        "interest_list": interest_list,
        "report_list": report_list,
    }
    return render(request, "posts/detail.html", context)


#  @login_required(login_url="/accounts/login/")
# def search(request):
#     q = request.GET.get("q")
#     category = request.GET.get("category", default="all")
#     option = request.GET.get("option", default="all")
#     sort = request.GET.get("sort", default="all")
#     post_list = Post.objects.filter(Q(name__icontains=q))
#     return render(request, "posts/search.html", context)
