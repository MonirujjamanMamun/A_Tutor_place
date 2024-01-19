from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.decorators import login_required
from . import models

# Create your views here.


@login_required
def add_tuition(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            tuition_form = forms.TuitionForms(request.POST)
            if tuition_form.is_valid():
                tuition_form.instance.author = request.user
                tuition_form.save()
                return redirect('home')

        else:
            tuition_form = forms.TuitionForms()
        return render(request, 'add_tuition.html', {'form': tuition_form})


@login_required
def edit_post(request, id):
    tuitions = models.TuitionsModel.objects.get(pk=id)
    tuitions_form = forms.TuitionForms(instance=tuitions)
    if request.method == 'POST':
        tuitions_form = forms.TuitionForms(request.POST, instance=tuitions)
        if tuitions_form.is_valid():
            tuitions_form.instance.author = request.user
            tuitions_form.save()
            return redirect('home')

    return render(request, 'add_tuition.html', {'form': tuitions_form})


@login_required
def delete_post(request, id):
    tuitions = models.TuitionsModel.objects.get(pk=id)
    tuitions.delete()
    return redirect('home')


@login_required
def userapplytotuition(request, id):
    tuitions = models.TuitionsModel.objects.get(pk=id)
    tuitions.is_apply = True
    tuitions.save()
    return redirect('home')
