from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Users
import random
import string

# Create your forms here.

class RegisterUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	name = forms.CharField(max_length=100, required=True)
	phone = forms.CharField(max_length=100, required=True)
	address = forms.CharField(max_length=100, required=True)
	shipping_address = forms.CharField(max_length=100, required=True)
	referral_token = forms.CharField(max_length=100, required=False)
	giver_token = forms.CharField(max_length=100, required=False)

	class Meta:
		model = Users
		fields = ("name", "email", "password1", "password2", "phone", "address", "shipping_address", "referral_token")

	def save(self, commit=True):
		user = super(RegisterUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.name = self.cleaned_data['name']
		user.phone = self.cleaned_data['phone']
		user.address = self.cleaned_data['address']
		user.shipping_address = self.cleaned_data['shipping_address']
		user.referral_token = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(32))
		if self.cleaned_data['referral_token']: self.giver_token = self.cleaned_data['referral_token']
		else : self.giver_token = None
		if commit:
			user.save()
		return user

	def is_valid(self) -> bool:
		return True
		return super().is_valid() and self.cleaned_data['password1'] == self.cleaned_data['password2']

	def referral_token_is_valid(self) -> bool:
		if self.cleaned_data['referral_token']:
			try:
				user = Users.objects.get(referral_token=self.cleaned_data['referral_token'])
				return True
			except Users.DoesNotExist:
				return False
		else:
			return True