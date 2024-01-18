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
    image = models.ImageField(upload_to="tuitions/images/")
    fee = models.IntegerField()
    cls = models.ManyToManyField(UserClassModel)
    tuition_types = models.CharField(
        choices=TUITION_TYPES, max_length=10, default="Pending")

    def __str__(self):
        return self.title


STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]


class ReviewModel(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    tuition = models.ForeignKey(TuitionsModel, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices=STAR_CHOICES, max_length=10)

    def __str__(self):
        return f"User -> {self.reviewer.first_name} ; Tuitions-> {self.tuition.user.first_name}"
