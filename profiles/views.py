from django.shortcuts import render, redirect
from tuitions.models import TuitionsModel
from users.models import UserAccountModels, UserAddressModel
# from django.views.generic import TemplateView

# Create your views here.


def userTuitions(request):
    tuition = TuitionsModel.objects.all()
    return render(request, 'tuitions_data.html', {'tuitions': tuition})


def adminAcceptedtotuition(request, id):
    tuitions = TuitionsModel.objects.get(pk=id)
    tuitions.is_apply = False
    tuitions.tuition_types = 'Accepted'
    tuitions.save()
    return redirect('home')


def user_profile(request, user_id):
    user_account = UserAccountModels.objects.get(user__id=user_id)
    user_address = UserAddressModel.objects.get(user__id=user_id)

    context = {
        'user_account': user_account,
        'user_address': user_address,
    }

    return render(request, 'profile.html', context)
