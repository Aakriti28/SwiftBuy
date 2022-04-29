from django import forms
from django.contrib.auth.forms import UserCreationForm
 
from user.models import Users, Paymentgateway
import random
import string

# Create your forms here.

class AddMoneyForm(forms.Form):
	amount = forms.IntegerField(required=True)
	payment_gateway = forms.ModelChoiceField(queryset=Paymentgateway.objects.all(), required=True)
	
	class Meta:
		model = Users
		fields = ("amount", "payment_gateway")

	def is_valid(self) -> bool :
		return super().is_valid()