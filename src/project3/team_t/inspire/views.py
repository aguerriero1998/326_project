from django.shortcuts import render
from inspire.models import Course, CourseInstance, Professor, Student, Days, CourseReview, ProfessorReview
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    if request.user.student.idnumber:
        print(f'/{request.user.student.idnumber}/')
        return HttpResponseRedirect(reverse('dashboard', args=(request.user.student.idnumber,)))
    else:
        print(request.user.student)
        return render(request, "index.html")

class Schedule(LoginRequiredMixin, generic.DetailView):
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


def class_search(request):
    context = {}
    return render(request, "class-search.html", context=context)

def search_results(request):
    context = {}

    return render(request, "search-results.html", context=context)

class ShoppingCartView(LoginRequiredMixin, generic.DetailView):
    model = Student
    template_name = "shopping-cart.html"


class StudentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Student
    template_name = "student-info.html"

class ProfessorDetailView(generic.DetailView):
    model = Professor
    template_name = "professor-info.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classes'] = CourseInstance.objects.all().filter(prof=self.object)
        print(ProfessorReview.objects.all().filter(professor=self.object).count())
        context['reviews'] = ProfessorReview.objects.all().filter(professor=self.object)
        return context


class StudentListView(generic.ListView):
    model = Student
    template_name = "students.html"

class CourseListView(generic.ListView):
    model = Course
    template_name = "courses.html"

class CourseInstanceListView(generic.ListView):
    model = CourseInstance
    template_name = "course-instances.html"

class ProfessorListView(generic.ListView):
    model = Professor
    template_name = "professors.html"

class CourseDetailView(generic.DetailView):
    model = Course
    template_name = "course-info.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(CourseReview.objects.all().filter(course=self.object))
        context['reviews'] = CourseReview.objects.all().filter(course=self.object)

        return context

class CourseInstanceDetailView(generic.DetailView):
    model = CourseInstance
    template_name = "course-instance-info.html"
   
