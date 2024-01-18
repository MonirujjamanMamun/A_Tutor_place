from django.shortcuts import render
from tuitions.models import TuitionsModel
# Create your views here.


def profile(request):
    tuition = TuitionsModel.objects.all()
    return render(request, 'profile_data.html', {'tuitions': tuition})
