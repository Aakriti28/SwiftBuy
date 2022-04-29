from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Users
import random
import string
import sys

# Create your forms here.

class RegisterUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	name = forms.CharField(max_length=100, required=True)
	phone = forms.CharField(max_length=100, required=True)
	address = forms.CharField(max_length=100, required=True)
	shipping_address = forms.CharField(max_length=100, required=False)
	referral_token = forms.CharField(max_length=100, required=False)
	giver_token = forms.CharField(max_length=100, required=False)
	role = forms.CharField(max_length=100, required=True)

	class Meta:
		model = Users
		fields = ("name", "email", "password", "phone", "address", "shipping_address", "referral_token")

	def save(self, commit=True):
		user = super(RegisterUserForm, self).save(commit=False)
		if self.cleaned_data['referral_token']: self.giver_token = self.cleaned_data['referral_token']
		else : self.giver_token = None
		if commit:
			user.save()
		return user

	def is_valid(self) -> bool:
		return super().is_valid()

	def referral_token_is_valid(self) -> bool:
		if self.cleaned_data['giver_token']:
			try:
				user = Users.objects.get(referral_token=self.cleaned_data['giver_token'])
				return True
			except Users.DoesNotExist:
				return False
		else:
			return True