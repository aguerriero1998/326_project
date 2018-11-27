from django.shortcuts import render
from inspire.models import Course, CourseInstance, Professor, Student, Days, CourseReview, ProfessorReview
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from functools import reduce
from .forms import reviewForm
from .forms import profReviewForm
from .forms import addCourseForm
from .forms import infoForm
from django.forms import ModelForm
from .forms import generalSearch, majorSearch, genedSearch
# Create your views here.

@login_required
def index(request):
    try:
        if request.user.student.idnumber:
            return HttpResponseRedirect(reverse('dashboard', args=(request.user.student.idnumber,)))
        else:
            return render(request, "course-instances.html")
    except:
        return HttpResponseRedirect(reverse("professor_list"))

class Schedule(LoginRequiredMixin, generic.DetailView):

    login_url = reverse('login')
    
    model = Student
    template_name = "dashboard.html"


    def get_list(self, day):
        courses_taking = self.object.coursesnow.all().filter(days__daysoffered=day)
        listOfdicts = []
        length = range(len(courses_taking))
        for p in courses_taking:
            dict = {"name": p.name,
            "room": p.location,
            "start": p.start.__str__()[0:5],
            "end": p.end.__str__()[0:5]}
            listOfdicts.append(dict)
        return listOfdicts


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["monday_classes"] = self.get_list("Mon")
        context["tuesday_classes"] = self.get_list("Tu")
        context["wednesday_classes"] = self.get_list("Wed")
        context["thursday_classes"] = self.get_list("Th")
        context["friday_classes"] = self.get_list("Fri")

        return context



class ShoppingCartView(LoginRequiredMixin, generic.DetailView):

    login_url = reverse('login')

    model = Student
    template_name = "shopping-cart.html"


class StudentDetailView(LoginRequiredMixin, generic.DetailView):
    
    login_url = reverse('login')

    model = Student
    template_name = "student-info.html"

class ProfessorDetailView(LoginRequiredMixin, generic.DetailView):

    login_url = reverse('login')

    model = Professor
    template_name = "professor-info.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classes'] = CourseInstance.objects.all().filter(prof=self.object)
        context['reviews'] = ProfessorReview.objects.all().filter(professor=self.object)
        return context


class StudentListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'inspire.can_view_student_list'

    model = Student
    template_name = "students.html"

class CourseListView(LoginRequiredMixin, generic.ListView):

    login_url = reverse('login')

    model = Course
    template_name = "courses.html"

def AddCourseReview(request,pk):

    course_to_review = Course.objects.get(coursenumber= pk)
    if request.method == 'POST':
        form = reviewForm(request.POST)
        request.POST.get('studentid', 'dne')
        if form.is_valid():
            stud = Student.objects.all().get(idnumber = request.POST.get("studentid"))
            r = CourseReview(remarks=form.cleaned_data['review'], giver=stud,course = course_to_review)
            r.save()
            return HttpResponseRedirect('success')
    else:
        form = reviewForm()
    context ={
        'course_to_review' : course_to_review,
        'form' : form,
    }
    return render(request, "add-course-review.html",context)

def Review_Success(request):
    return render(request, "review_success.html")

def editInfo(request,pk):
    s = Student.objects.all().get(idnumber = pk)
    name = s.name
    if request.method == "POST":
        form = infoForm(request.POST)
        if form.is_valid():
            s.address = form.cleaned_data['address']
            s.phonenumber = form.cleaned_data['phonenumber']
            s.emergency = form.cleaned_data['emergency']
            s.gender = form.cleaned_data['gender']
            s.pronouns = form.cleaned_data['pronouns']
            s.save()
            url = '{}{}'.format('/inspire/student-info/',pk)
            return HttpResponseRedirect(url)
    else:
        form = infoForm(initial = {'address': s.address, 'phonenumber': s.phonenumber, 'emergency': s.emergency, 'gender': s.gender, 'pronouns': s.pronouns})
    context = {
        'form' : form,
        's': s,
        'name': name
    }
    return render(request, "edit-info.html", context)


def AddProfessorReview(request,pk):
    prof_to_review = Professor.objects.get(name= pk)
    if request.method == 'POST':
        form = reviewForm(request.POST)
        if form.is_valid():
            stud = Student.objects.all().filter(idnumber = request.POST.get("studentid")).get()
            r = ProfessorReview(remarks=form.cleaned_data['review'], giver=stud, professor=prof_to_review)
            r.save()
            return HttpResponseRedirect("success")
    else:
        form = profReviewForm()
    context ={
        'prof_to_review' : prof_to_review,
        'form' : form,
    }
    return render(request, "add-professor-review.html",context)

def AddProfessorReviewSuccess(request,pk):
    return render(request, "review_success.html")

def add_course(request):
    if request.method == "POST":
        form = addCourseForm(request.POST)
        if form.is_valid():
            c = Course(name=form.cleaned_data['name'], coursenumber=form.cleaned_data['coursenumber'], description=form.cleaned_data['description'], credits=form.cleaned_data['credits'], gened=form.cleaned_data['gened'], major=form.cleaned_data['major'], rating = 0 )
            c.save()
            return HttpResponseRedirect('add-course')
    else:
        form = addCourseForm()
    context ={
        'form' : form,
    }
    return render(request, "add-course.html", context)
    

class CourseInstanceListView(LoginRequiredMixin, generic.ListView):
    
    login_url = reverse('login')

    model = CourseInstance
    template_name = "course-instances.html"

class ProfessorListView(LoginRequiredMixin, generic.ListView):
    
    login_url = reverse('login')
    
    model = Professor
    template_name = "professors.html"

class CourseDetailView(LoginRequiredMixin, generic.DetailView):

    login_url = reverse('login')

    model = Course
    template_name = "course-info.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = CourseReview.objects.all().filter(course=self.object)

        return context

class CourseInstanceDetailView(LoginRequiredMixin, generic.DetailView):

    login_url = reverse('login')

    model = CourseInstance
    template_name = "course-instance-info.html"
   
def unenroll_classes(request):


    courses = request.POST.getlist('courseId')
    student_id = request.POST.get('studentid', '')

    student = Student.objects.all().filter(idnumber=student_id).get()

    [student.coursesnow.remove(CourseInstance.objects.all().filter(classnumber=course).get()) for course in courses]

    return HttpResponseRedirect(reverse("shopping_cart", args=(student_id,)))

def enroll_classes(request):

    def enroll(course, student):

        # Queries for all courses that meet on the same day as the course that is being enrolled. It uses the Q function to query the database
        potential_conflicts = student.coursesnow.all().filter(reduce(lambda x, y: x | y, [Q(days__daysoffered__contains=day['daysoffered']) for day in course.days.all().values()]))

        for pcourse in potential_conflicts:
            if(pcourse.start <= course.start <= pcourse.end or pcourse.start <= course.end <= pcourse.end):
                return course
            
                
        student.coursesnow.add(course)
        student.shoppingcart.remove(course)    
        return None    



    def remove(course, student):
        student.shoppingcart.remove(course)


    courses = request.POST.getlist('courseId')
    student_id = request.POST.get('studentid', '')

    student = Student.objects.all().filter(idnumber=student_id).get()

    if "enroll" in request.POST:
        result = [enroll(CourseInstance.objects.all().filter(classnumber=course).get(), student) for course in courses]
        result = filter(lambda x: x is not None, result)
        if result:
            for course in result:
                messages.info(request, f"Could not enroll in course  '{course} : {course.classnumber}' due to a conflict")
        
    
    if "delete" in request.POST:
        [remove(CourseInstance.objects.all().filter(classnumber=course).get(), student) for course in courses] 

    return HttpResponseRedirect(reverse("shopping_cart", args=(student_id,)))

def add_to_shopping_cart(request):
    
    courses = request.POST.getlist('courseId')
    student_id = request.POST.get('studentid', 'Doesnt exist')

    student = Student.objects.all().filter(idnumber=student_id).get()
   
    # student.shoppingcart.add()
    [student.shoppingcart.add(CourseInstance.objects.all().filter(classnumber=course).get()) for course in courses if (not student.shoppingcart.all().filter(classnumber=course).exists() and not student.coursesnow.all().filter(classnumber=course).exists())]

    return HttpResponseRedirect(reverse("shopping_cart", args=(student_id,)))






@login_required
def class_search(request):
    return render(request, "class-search.html")

@login_required
def search_results_general(request):

    if (request.method == 'POST'):
    #if (request.POST.get('button')):
   
        form = generalSearch(request.POST)
        
        #form = searchFrom(request.POST)
        #the_course = course.objects.all()
        if form.is_valid():
            print("THIS WORKS")
            the_coursenum = Course.objects.filter(coursenumber=form.cleaned_data["num"]).first()
            #the_subject = Course.object.all().get(major = form.cleaned_data['subject'])
            #the_credit_amount = Course.object.all().get(credits = form.cleaned_data["credit_amount"])
            
            print(form.cleaned_data['keyword'])
            
            the_course = Course.objects.filter(
                                       Q(name__contains = form.cleaned_data['keyword']) |
                                       Q(description__contains = form.cleaned_data['keyword'])).distinct().first()
                                       
            instances = CourseInstance.objects.filter(basecourse=the_course)
            
            if the_course is None:
                return render(request, "search-results.html")
                                                        
                                                        #results = Course.objects.filter()
            
                                                        #return HttpResponseRedirect('search-results')
                                        
            return render(request, "search-results.html", context={'results':[{"name":the_course.name, "instances":instances}]})
        print(form.errors)


    else:
        the_course = []
        print("askjdfhas")
        return render(request, "search-results.html")
        #return render(request, "search-results.html", {'the_course': course, 'form':form})
        #return HttpResponseRedirect('search-results')
#return render(request, "search-results.html", {'the_course': course, 'form':form})
    return render(request, "search-results.html")
    
"""
@login_required
def search_results_major(request):
    if(request.method == "POST"):
        form = majorsearchform(request.POST)
        if form.is_valid:
            the_major_selection = course.objects.get(major = form.cleaned_data['sel_major'])
            the_major_keyword = courses.filter(
                            Q(coursename__contains = query) |
                            Q(description__contains = query)).distinct()
            return render(request, "search-results.html")
    else:
        return render(request, "search-results.html")
    return render(request, "search-results.html")

        #category



@login_required
def search_results_gened(request):
    if(request.method == "POST"):
        form = genedsearchform(request.POST)
        if form.is_valid:
            gened_sel = course.objects.get(gened = form.cleaned_data['gened_sel'])
            gened_keyword = courses.filter(Q(coursename__contains = query) |
                                           Q(description__contains = query)).distinct()
            
            return render(request, "search-results.html")
    else:
          return render(request, "search-results.html")
    return render(request, "search-results.html")
                                           
                                                        





    
#class search
def general_Search(request):
    if request.method == "POST":
       gen_search_form = form(request.POST)
    #form = forms.generalsearch(request.POST)
    #query = request.GET.get('q')
    #if request.method == 'POST':
        #form = generalSearch(request.POST)
       #courses = course.objects.all()
       
       #course = courses.filter(
                            Q(coursename__contains = query) |
                            Q(description__contains = query)).distinct()
       if gen_search_form.is_valid():
        the_course = Course.objects.get(name=gen_search_form.cleaned_data["course-keyword"])
        return render_to_response("search-result.html",{'the_course': the_course },context_instance = RequestContext(request) )
    else:
        the_course = generalSearch()
    return render_to_response("search-page.html", {'gen_search_form': gen_search_form},context_instance= RequestContext(request) )

    

            if(course_number == "is exactly"):
                course_number = couse.objects.all().filter(coursenumber =request.POST.get("course_number")).get()
            else if(course_number == "starts with"):
                course_number = course.objects.filter(course__coursenumber__startswith = request.POST.get("course_number"))
            else if(course_number == "greater than equal to"):
                course_number = course.objects.filter(course__coursenumber >= request.POST.get("course_number"))
            else if(course_number == "contains"):
                course_number = course.objects.filter(course__coursenumber__contains = request.POST.get("course_number"))
            
            

#return HttpResponseRedirect("search-result")




#context = RequestContext(request)


#return render_to_response('search-results.html', context_instance = RequestContext(request))

        class_number = courseInstance.objects.all().get(coursenumber = form.cleaned_data['class_number'])
        course_subject = course.objects.all().get(major = form.cleaned_data['course_subject;])
        course_number = course.object.all().get(coursenumber = form.cleaned_data['course_number'])
                                                                            #make wuery set
        course_keyword =
        career_type = 
        instructor_name = courseInstance.objects.all().get(prof = form.cleaned_data['instructor_name'])
        credit_amount = course.objects.all().get(credits = form.cleaned_data['credit_amount'])
        mode_of_instruction = course.objects.all().get(mode_of_instruction = form.cleaned_data['mode_of_instruction'])
        rap = course.objects.get()(rap = form.cleaned_data['rap'])
        cpe = course.objects.get()(cpe = form.cleaned_data['cpe'])
        

    else:
        form = generalsearch
        context = {}
        return render(request, "search-results.html")
        the_course = Course.objects.get(name=gen_search_form.cleaned_data["course-keyword"])
"""

