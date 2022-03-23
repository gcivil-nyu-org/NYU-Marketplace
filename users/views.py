from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile

# Create your views here.


def profile(request):
    if request.method == "POST":
        profile = Profile.objects.create(user=request.user)
        form = ProfileForm(request.POST, instance=profile)
        form.save()
        return redirect("http://127.0.0.1:8000/posts/")
    else:
        form = ProfileForm()
    return render(request, "users/profile.html", {"form": form})
