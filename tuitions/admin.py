from django.contrib import admin
from . import models
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Register your models here.


class UserClassAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(models.UserClassModel, UserClassAdmin)
admin.site.register(models.ReviewModel)
admin.site.register(models.TuitionsModel)
