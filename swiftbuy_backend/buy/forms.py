from django import forms

import random
import string

# Create your forms here.

class AddReviewForm(forms.Form):
    review = forms.CharField(max_length=1000, required=True)
    rating = forms.IntegerField(required=True)
    product_id = forms.IntegerField(required=True)
    user_id = forms.IntegerField(required=True)

    def save(self, commit=True):
        review = super(AddReviewForm, self).save(commit=False)
        review.review = self.cleaned_data['review']
        review.rating = self.cleaned_data['rating']
        review.product_id = self.cleaned_data['product_id']
        review.user_id = self.cleaned_data['user_id']
        if commit:
            review.save()
        return review

    def is_valid(self) -> bool:
        return super().is_valid() and self.cleaned_data['rating'] >= 1 and self.cleaned_data['rating'] <= 5

