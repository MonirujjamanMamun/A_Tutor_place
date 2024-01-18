from django.shortcuts import render
from django.views.generic import TemplateView
from tuitions.models import TuitionsModel, UserClassModel
# Create your views here.


# class HomeView(TemplateView):
#     template_name = 'home.html'


def home(request, slugs=None):
    tuition = TuitionsModel.objects.all()
    if slugs is not None:
        cls = UserClassModel.objects.get(slug=slugs)
        tuition = TuitionsModel.objects.filter(cls=cls)
    cls = UserClassModel.objects.all()
    return render(request, 'home.html', {"tuitions": tuition, 'cls': cls})
