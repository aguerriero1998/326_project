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
# Create your views here.

@login_required
def index(request):
    try:
        if request.user.student.idnumber:
            return HttpResponseRedirect(reverse('dashboard', args=(request.user.student.idnumber,)))
        else:
            return render(request, "course-instances.html")
    except:
        return render(request, "professors.html")

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

@login_required
def class_search(request):
    return render(request, "class-search.html")

@login_required
def search_results(request):
    return render(request, "search-results.html")

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

