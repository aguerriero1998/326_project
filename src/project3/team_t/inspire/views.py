from django.shortcuts import render
from inspire.models import Course, CourseInstance, Professor, Student, Days, CourseReview, ProfessorReview
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
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
        print(courses_taking)
        listOfdicts = []
        length = range(len(courses_taking))
        for p in courses_taking:
            print(p.start.__str__()[0:5])
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
        print(ProfessorReview.objects.all().filter(professor=self.object).count())
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
        print(CourseReview.objects.all().filter(course=self.object))
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

    print(student.coursesnow.all())
    

    [student.coursesnow.remove(CourseInstance.objects.all().filter(classnumber=course).get()) for course in courses]

    return HttpResponseRedirect(reverse("shopping_cart", args=(student_id,)))
    
