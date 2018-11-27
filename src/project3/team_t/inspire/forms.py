from django import forms
from django.forms import ModelForm
from inspire.models import Course, Student, CourseInstance


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

### class search stuff
class generalSearch(forms.Form):
    #class-number = forms.IntegerField(null = True, black = True)
    subject = forms.ChoiceField(required=False)
    num= forms.IntegerField(required=False)
    keyword = forms.CharField(required=False)
    #sel_cat= forms.ChoiceField(required = False)
    #instructor_name = instructor-sel
    credit_amount = forms.ChoiceField(required=False)
    #mode_of_instruction = forms.ChoiceField(required = False)
    #sel_rap = forms.ChoiceField(required = False)
#sel_cpe = forms.ChoiceField(required = False)

class majorSearch(forms.Form):
    sel_major = forms.ChoiceField()
    majorsel_cat= forms.ChoiceField()
    majorkeyword = forms.ChoiceField()

class genedSearch(forms.Form):
    gened_sel = forms.ChoiceField()
    gened_keyword = forms.CharField()




"""
    class_number = forms.IntegerField(help_text = "Enter a class Number to search" , required = false)
    course_subject = forms.ChoiceField()
    #course_number =  forms.IntegerField(primary_key=True, validators=[MaxValueValidator(80000), MinValueValidator(70000)])
    course_keyword = forms.CharField(help_text = "enter a keyword for the course", blank = True)

##### advanced
    career_type = forms.ChoiceField(label = "", initial = '', weidget = forms.select(),required = false)
    instructor_name_selection =forms.charField(label = "", initial = '', weidget = forms.select(),required = false)
    instructor_name = forms.ChoiceField(label = "", initial = '', weidget = forms.select(),required = false)
    credit_amount = forms.ChoiceField(label = "", initial = '', weidget = forms.select(),required = false)
    mode_of_instruction = forms.ChoiceField(label = "", initial = '', weidget = forms.select(),required = false)
    rap = forms.ChoiceField(label = "", initial = '', weidget = forms.select(),required = false)
    cpe = forms.ChoiceField(label = "", initial = '', weidget = forms.select(),required = false)
"""
"""
class majorSearch(forms.Form)
    major = forms.ChoiceField()
    category = forms.ChoiceField()
    keyword = forms.CharField()

"""
