from django.shortcuts import render
from inspire.models import Course, CourseInstance, Professor, Student, Days
from django.views import generic

# Create your views here.
def dashboard(request):
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
    def get_list(day):
        student = Student.objects.filter(idnumber = self.idnumber)
        course_taking = student.objects
        listOfdicts = []
        length = range(len(q1))
        for i in length:
            dict = {"key": q1[i].name, }
            listOfdicts.append(dict)
    
    context = {}

    """context = {
        monday_classes = get_list("monday")
        tuesday_classes = get_list("tuesday")
        wednesday_classes = get_list("wednesday")
        thursday_classes = get_list("thursday")
        friday_classes = get_list("friday")
    }"""
    # Render the HTML template index.html with the data in the context variable
    return render(request, "dashboard.html", context=context)

def class_search(request):
    context = {}
    return render(request, "class-search.html", context=context)

def search_results(request):
    context = {}

    return render(request, "search-results.html", context=context)

def shopping_cart(request):
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
    template_name = "course-description.html"

