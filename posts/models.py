from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    name = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, "Name must be at least 2 characters long")],
    )
    description = models.TextField(
        max_length=400,
        validators=[
            MinLengthValidator(2, "Description must be at least 2 characters long")
        ],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    options = (
        ("sell", "Sell"),
        ("rent", "Rent"),
        ("exchange", "Exchange"),
    )
    option = models.CharField(max_length=10, choices=options, default="Rent")
    categories = (
        ("textbook", "Textbook"),
        ("tech", "Tech"),
        ("sport", "Sport"),
        ("furniture", "Furniture"),
        ("other", "Other"),
    )
    category = models.CharField(max_length=10, choices=categories, default="Textbook")
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    location = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2, "Location must be greater than 2 characters long")
        ],
    )

    # Picture
    picture = models.ImageField(null=True, editable=True)
    # content_type = models.CharField(max_length=256, null=True, help_text='The MIMEType of the file')
    report_count = models.PositiveIntegerField(default=0)
    interested_count = models.PositiveIntegerField(default=0)

    # Shows up in the admin list
    def __str__(self):
        return self.name


class Report(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reasons = (
        ("1", "Inappropriate post content"),
        ("2", "Post item is unavailable anymore"),
        ("3", "Cannot reach out to post owner"),
        ("4", "Other"),
    )
    reason = models.IntegerField(max_length=10, choices=reasons, default=4)

    class Meta:
        unique_together = ("post", "reported_by")


class Interest(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    interested_user = models.ForeignKey(User, on_delete=models.CASCADE)
    cust_message = models.TextField(
        max_length=400,
        validators=[MinLengthValidator(2, "Title must be greater than 2 characters")],
        null=True,
    )

    class Meta:
        unique_together = ("post", "interested_user")

    def __str__(self):
        return f"{self.interested_user.username} interested in {self.post}"
