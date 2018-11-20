from django import forms

class reviewForm(forms.Form):
    giver = forms.CharField(label= "Student ID ", max_length = 20)
    review = forms.CharField(label='Review ', max_length=1000, widget=forms.Textarea)
    

class profReviewForm(forms.Form):
    giver = forms.CharField(label= "Student ID ", max_length = 20)
    review = forms.CharField(label='Review ', max_length=1000, widget=forms.Textarea)


