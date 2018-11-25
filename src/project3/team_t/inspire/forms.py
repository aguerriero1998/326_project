from django import forms
from django.forms import ModelForm
from inspire.models import Course, Student

class reviewForm(forms.Form):
    review = forms.CharField(label='Review ', max_length=1000, widget=forms.Textarea)
    

class profReviewForm(forms.Form):
    review = forms.CharField(label='Review ', max_length=1000, widget=forms.Textarea)

class addCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'coursenumber', 'description', 'credits', 'gened', 'major']
        
class infoForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['address', 'phonenumber', 'emergency', 'gender', 'pronouns']


        """address = forms.CharField(required=False)
        phonenumber = forms.CharField(required=False)
        emergency = forms.CharField(required = False)
        gender = forms.CharField(required = False)
        pronouns = forms.CharField(required = False)
        initial = {'address': s.address, 'phonenumber': s.phonenumber, 'emergency': s.emergency, 'gender': s.gender, 'pronouns': s.pronouns}"""

