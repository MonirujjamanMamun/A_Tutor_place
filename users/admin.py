from django.contrib import admin
from users.models import UserAddressModel, UserAccountModels
# Register your models here.

admin.site.register(UserAddressModel)
admin.site.register(UserAccountModels)
