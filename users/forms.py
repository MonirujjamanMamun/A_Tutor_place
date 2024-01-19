from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import UserAccountModels, UserAddressModel
from . constants import GENDER_TYPE


class UserRegistrationForm(UserCreationForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    postal_code = forms.IntegerField()
    education = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name',
                  'email', 'birth_date', 'gender', 'postal_code', 'city', 'education', 'street_address']

    def save(self, commit=True):
        our_user = super().save(commit=False)
        if commit == True:
            our_user.save()
            gender = self.cleaned_data.get('gender')
            postal_code = self.cleaned_data.get('postal_code')
            education = self.cleaned_data.get('education')
            birth_date = self.cleaned_data.get('birth_date')
            city = self.cleaned_data.get('city')
            street_address = self.cleaned_data.get('street_address')

            UserAddressModel.objects.create(
                user=our_user,
                postal_code=postal_code,
                city=city,
                street_address=street_address
            )
            UserAccountModels.objects.create(
                user=our_user,
                education=education,
                gender=gender,
                birth_date=birth_date
            )
        return our_user


class UserUpdateForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    education = forms.CharField(max_length=100)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    postal_code = forms.IntegerField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance:
            try:
                user_account = self.instance.account
                user_address = self.instance.address
            except UserAccountModels.DoesNotExist:
                user_account = None
                user_address = None

            if user_account:
                self.fields['education'].initial = user_account.education
                self.fields['gender'].initial = user_account.gender
                self.fields['birth_date'].initial = user_account.birth_date
                self.fields['street_address'].initial = user_address.street_address
                self.fields['city'].initial = user_address.city
                self.fields['postal_code'].initial = user_address.postal_code

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

            user_account, created = UserAccountModels.objects.get_or_create(
                user=user)
            user_address, created = UserAddressModel.objects.get_or_create(
                user=user)

            user_account.education = self.cleaned_data['education']
            user_account.gender = self.cleaned_data['gender']
            user_account.birth_date = self.cleaned_data['birth_date']
            user_account.save()

            user_address.street_address = self.cleaned_data['street_address']
            user_address.city = self.cleaned_data['city']
            user_address.postal_code = self.cleaned_data['postal_code']
            user_address.save()

        return user
