from django.shortcuts import render, redirect
from . import forms
# Create your views here.


def add_tuition(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            post_form = forms.TuitionForms(request.POST)
            if post_form.is_valid():
                # post_form.cleaned_data['author'] = request.user
                post_form.instance.author = request.user
                post_form.save()
                return redirect('home')

        else:  # user normally website e gele blank form pabe
            post_form = forms.TuitionForms()
        return render(request, 'add_tuition.html', {'form': post_form})
