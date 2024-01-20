from django.db import models
from tuitions.models import TuitionsModel
# Create your models here.


class CommentModel(models.Model):
    tuition = models.ForeignKey(
        TuitionsModel, on_delete=models.CASCADE, related_name='tuitions')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
