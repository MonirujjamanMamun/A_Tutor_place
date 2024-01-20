from django.shortcuts import render, redirect
from tuitions.models import TuitionsModel
from django.views.generic import TemplateView
# from tuitions.forms import ReviewForms
# from users.models import UserAccountModels, UserAddressModel
# Create your views here.


def userTuitions(request):
    tuition = TuitionsModel.objects.all()
    # review = ReviewModel.objects.all()
    return render(request, 'tuitions_data.html', {'tuitions': tuition})


def adminAcceptedtotuition(request, id):
    tuitions = TuitionsModel.objects.get(pk=id)
    tuitions.is_apply = False
    tuitions.tuition_types = 'Accepted'
    tuitions.save()
    return redirect('home')


# def profile(request):
#     userAccountData = UserAccountModels.objects.all()
#     userAddressData = UserAddressModel.objects.all()
#     return render(request, 'profile.html', {'accountData': userAccountData, 'addressData': userAddressData})
class Profile(TemplateView):
    template_name = 'profile.html'
