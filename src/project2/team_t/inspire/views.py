from django.shortcuts import render
from inspire.models import Course, CourseInstance, Professor, Student, Days
from django.views import generic

# Create your views here.
def dashboard(request, idnumber):
    def get_list(day):
        courses_taking = CourseInstance.objects.filter(days__name = day)
        courses_taking = courses_taking.filter(studentname__idnumber = idnumber)
        listOfdicts = []
        length = range(len(courses_taking))
        for p in courses_taking:
            dict = {"name": p.name,
            "room": p.location,
            "start": p.start,
            "end": p.end}
            listOfdicts.append(dict)
        return listOfdicts

    context = {
        "monday_classes": get_list("monday"),
        "tuesday_classes": get_list("tuesday"),
        "wednesday_classes": get_list("wednesday"),
        "thursday_classes": get_list("thursday"),
        "friday_classes": get_list("friday"),
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, "dashboard.html", context=context)

def class_search(request):
    context = {}
    return render(request, "class-search.html", context=context)

def search_results(request):
    context = {}

    return render(request, "search-results.html", context=context)

def shopping_cart(request, pk):
    context = {}

    return render(request, "ShoppingCart.html", context=context)

class studentinfo(generic.DetailView):
    model = Student
    template_name = "studentinfo.html"

class profDetailView(generic.DetailView):
    model = Professor
    template_name = "professors.html"

class courseDetailView(generic.DetailView):
    model = Course
    template_name = "courseinfo.html"

    """View function for home page of site.
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact="a").count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
    }
    """
