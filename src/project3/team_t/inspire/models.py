from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    """
        Model representing a course at UMass (e.g CS326, CS311).
        Inlcudes the description, course number, credits, rating, and other attributes.
        Not to be confused with a CourseInstance which is the actual class session which has a time, location, ect.
    """

    name = models.CharField(max_length=20, help_text='Enter a class name')
    coursenumber = models.IntegerField(primary_key=True, validators=[MaxValueValidator(80000), MinValueValidator(70000)])
    description =  models.TextField(max_length=100)
    credits =  models.IntegerField(validators=[MaxValueValidator(4), MinValueValidator(1)])
    rating =  models.DecimalField(max_digits=3, decimal_places=2)
    gened =  models.CharField(max_length=3)
    major =  models.CharField(max_length=25)
    recommendations =  models.ManyToManyField('CourseInstance')
    
    
    def __str__(self):
        return self.name
    def get_recommendations(self):
        return ", ".join(recommendations.name for recommendations in self.recommendations.all()[:5])
    get_recommendations.short_description = "recommendations"


class CourseInstance(models.Model):

    """
        A session of a Course. It includes a professor, class number, time, location, textbook, enrollment information, ect.
        base_course points to the Course which this object represents (Similar to BookInstance and Book in Django Library Example). 
    """
    
    name = models.CharField(max_length=20, help_text='Enter a class name')

    prof = models.ForeignKey('Professor', on_delete=models.SET_NULL, null=True)
    classnumber = models.IntegerField(primary_key=True, validators=[MaxValueValidator(1000), MinValueValidator(1)])
    prerequisites = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True, related_name='prerequisites', blank = True) # TO RECONSIDER ....

    start = models.TimeField(null=True, blank=True) 
    end = models.TimeField(null=True, blank=True)
    semester = models.CharField(max_length=6)
    location = models.CharField(max_length=25)
    textbook = models.CharField(max_length=25)
    students = models.IntegerField(validators=[MaxValueValidator(500), MinValueValidator(0)])
    available = models.IntegerField(validators=[MaxValueValidator(500), MinValueValidator(0)])

    days = models.ManyToManyField("Days")

    basecourse = models.ForeignKey("Course", on_delete=models.SET_NULL, null=True, related_name='basecourse')
    
    def __str__(self):
        return self.name
    def get_days(self):
        return ", ".join(days.daysoffered for days in self.days.all()[:5])
    get_days.short_description = "Days"

class Professor(models.Model):

    """
        Professor object, with a name and rating
    """
    name = models.CharField(primary_key=True, max_length=20, help_text='Enter a name')
    rating =  models.DecimalField(max_digits=3, decimal_places=2, null=True)

    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Student(models.Model):
    """
        Represents a student with personal information such as student ID, email, ect. 
        and class information, i.e courses currently enrolled in, ect.
    """
    name = models.CharField(max_length=25)
    idnumber = models.IntegerField(primary_key=True, validators=[MaxValueValidator(40000000), MinValueValidator(30000000)])
    phonenumber = models.CharField(max_length=12)
    address = models.CharField(max_length=60)
    gender = models.CharField(max_length=25)
    
    pronouns = models.CharField(max_length=25)
    emergency = models.CharField(max_length=25)

    coursestaken = models.ManyToManyField('CourseInstance')
    coursesnow = models.ManyToManyField("CourseInstance", related_name='coursesnow')
    shoppingcart = models.ManyToManyField('CourseInstance', related_name='shoppingcart')

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name
    
    def get_shoppingcart(self):
        return ", ".join(shoppingcart.name for shoppingcart in self.shoppingcart.all())
    get_shoppingcart.short_description = "Shopping Cart"

    def get_coursestaken(self):
        return ", ".join(coursestaken.name for coursestaken in self.coursestaken.all())
    get_coursestaken.short_description = "Courses Taken"

    class Meta:
        permissions = (("can_view_student_list", "Can view the list of student view"),)


class Days(models.Model):
    """
        A Day Model, represents a day on which a CourseInstance will meet. Only 5 choices here
    """

    OFFERED = (
            ("Mon", "Monday"),
            ("Tu", "Tuesday"),
            ("Wed", "Wednesday"),
            ("Th", "Thursday"),
            ("Fri", "Friday"),
    )

    daysoffered = models.CharField(
            max_length=3,
            choices=OFFERED,
            blank=True,
            default="Mon",
            help_text="Days offered",
    )

    def __str__(self):
        return self.daysoffered

class ProfessorReview(models.Model):

    """
        Represents A review given to a professor consisting of the actual comment, the student who gave the review, 
        and professor which was reviewed
    """
    
    remarks = models.TextField(max_length=200)
    giver = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True)

    professor = models.ForeignKey('Professor', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.remarks[0:30]


class CourseReview(models.Model):

    """
        Represents A review given to a course consisting of the actual comment, the student who gave the review, 
        and course which was reviewed
    """

    remarks = models.TextField(max_length=200)
    giver = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.remarks

