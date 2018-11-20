from django import forms
from django.forms import ModelForm
from inspire.models import Course

class reviewForm(forms.Form):
    giver = forms.CharField(label= "Student ID ", max_length = 20)
    review = forms.CharField(label='Review ', max_length=1000, widget=forms.Textarea)
    

class profReviewForm(forms.Form):
    giver = forms.CharField(label= "Student ID ", max_length = 20)
    review = forms.CharField(label='Review ', max_length=1000, widget=forms.Textarea)

class addCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'coursenumber', 'description', 'credits', 'gened', 'major']

