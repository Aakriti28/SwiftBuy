from django import forms
from django.contrib.auth.forms import UserCreationForm
 
from user.models import Users, Paymentgateway
import random
import string

# Create your forms here.

class AddMoneyForm(UserCreationForm):
	amount = forms.IntegerField(required=True)
	payment_gateway = forms.ModelChoiceField(queryset=Paymentgateway.objects.all(), required=True)
	
	class Meta:
		model = Users
		fields = ("amount", "payment_gateway")

	def save(self, commit=True):
		user = super(AddMoneyForm, self).save(commit=False)
		user.amount = self.cleaned_data['amount']
		user.payment_gateway = self.cleaned_data['payment_gateway']
		if commit:
			user.save()
		return user