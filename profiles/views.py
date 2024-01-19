from django.shortcuts import render, redirect
from tuitions.models import TuitionsModel, ReviewModel
from tuitions.forms import ReviewForms
from users.models import UserAccountModels, UserAddressModel
# Create your views here.


def userTuitions(request):
    tuition = TuitionsModel.objects.all()
    review = ReviewModel.objects.all()
    return render(request, 'tuitions_data.html', {'tuitions': tuition, 'reviews': review})


def adminAcceptedtotuition(request, id):
    tuitions = TuitionsModel.objects.get(pk=id)
    tuitions.is_apply = False
    tuitions.tuition_types = 'Accepted'
    tuitions.save()
    return redirect('home')


def tuitionReview(request):
    if request.method == 'POST':
        review_form = ReviewForms(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect('usertuitions')
    else:
        review_form = ReviewForms()
    return render(request, 'review_form.html', {'form': review_form})


def profile(request):
    userAccountData = UserAccountModels.objects.all()
    userAddressData = UserAddressModel.objects.all()
    return render(request, 'profile.html', {'accountData': userAccountData, 'addressData': userAddressData})
