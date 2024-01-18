from django import forms
from . import models


class TuitionForms(forms.ModelForm):
    class Meta:
        model = models.TuitionsModel
        # fields = '__all__'
        exclude = ['user']


class ReviewForms(forms.ModelForm):
    model = models.ReviewModel
    fields = '__all__'


class ClassModel(forms.ModelForm):
    model = models.UserClassModel
    fields = '__all__'
