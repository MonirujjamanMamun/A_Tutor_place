from django import forms
from . import models


class TuitionForms(forms.ModelForm):
    class Meta:
        model = models.TuitionsModel
        # fields = '__all__'
        exclude = ['user', 'is_apply']


class ReviewForms(forms.ModelForm):
    class Meta:
        model = models.ReviewModel
        fields = ['name', 'body']


class ClassModel(forms.ModelForm):
    model = models.UserClassModel
    fields = '__all__'
