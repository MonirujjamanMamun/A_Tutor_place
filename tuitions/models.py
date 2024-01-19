from django.db import models
from django.contrib.auth.models import User
# Create your models here.
TUITION_TYPES = [
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
]


class UserClassModel(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=65)

    def __str__(self):
        return self.name


class TuitionsModel(models.Model):
    # user = models.OneToM(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    # books_img = models.ImageField(
    #     upload_to='tuitions/media/uploads/', blank=True, null=True)
    fee = models.IntegerField()
    cls = models.ManyToManyField(UserClassModel)
    is_apply = models.BooleanField(default=False)
    tuition_types = models.CharField(
        choices=TUITION_TYPES, max_length=10, default="Pending")

    def __str__(self):
        return self.title


class ReviewModel(models.Model):
    post = models.ForeignKey(
        TuitionsModel, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"Comments by {self.name}"
