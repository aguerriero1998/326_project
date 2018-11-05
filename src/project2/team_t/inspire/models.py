from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Course(models.Model):
    """
        Model representing a course at UMass (e.g CS326, CS311).
        """
    name = models.CharField(max_length=20, help_text='Enter a class name')
    coursenumber = models.IntegerField(validators=[MaxValueValidator(80000), MinValueValidator(70000)])
    description =  models.TextField(max_length=100)
    credits =  models.IntegerField(validators=[MaxValueValidator(4), MinValueValidator(1)])
    rating =  models.DecimalField(max_digits=3, decimal_places=2)
    comments =  models.TextField(max_length=100)
    gened =  models.CharField(max_length=3)
    major =  models.CharField(max_length=25)
    reccomendation =  models.ForeignKey('Course', on_delete=models.SET_NULL, null=True, blank = True)
    
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class CourseInstance(models.Model):
    
    name = models.CharField(max_length=20, help_text='Enter a class name')
    prof = models.ForeignKey('Professor', on_delete=models.SET_NULL, null = True, blank = True)
    classnumber = models.IntegerField(validators=[MaxValueValidator(1000), MinValueValidator(1)])
    prerequisites = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True, related_name='prerequisites', blank = True)
    start = models.TimeField(null=True, blank=True) 
    end = models.TimeField(null=True, blank=True)
    semester = models.CharField(max_length=6)
    location = models.CharField(max_length=25)
    textbook = models.CharField(max_length=25)
    students = models.IntegerField(validators=[MaxValueValidator(500), MinValueValidator(0)])
    available = models.IntegerField(validators=[MaxValueValidator(500), MinValueValidator(0)])
    days = models.ManyToManyField("Days", blank = True)
    studentname = models.ManyToManyField("Student", blank = True)
    basecourse = models.ForeignKey("Course", on_delete=models.SET_NULL, null=True, related_name='basecourse')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    def get_days(self):
        return ", ".join(days.daysofweek for days in self.days.all()[:7])
    get_days.short_description = "Days"

class Professor(models.Model):
    name = models.CharField(max_length=20, help_text='Enter a name')

    taught = models.ForeignKey('CourseInstance', on_delete=models.SET_NULL, null = True, blank = True)
    review = models.ManyToManyField('Reviews', null = True, blank = True)
    rating =  models.DecimalField(max_digits=3, decimal_places=2)
    def get_reviews(self):
        return ", ".join(review.remarks for review in self.review.all())
    get_reviews.short_description = "Reviews"


    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=25)
    idnumber = models.IntegerField(validators=[MaxValueValidator(40000000), MinValueValidator(30000000)])
    email = models.EmailField(max_length=25)
    phonenumber = models.CharField(max_length=12)
    gender = models.CharField(max_length=25)
    pronouns = models.CharField(max_length=25)
    emergency = models.CharField(max_length=25)
    coursestaken = models.ManyToManyField('Course',  blank = True)
    coursesnow = models.ManyToManyField('CourseInstance', related_name='coursesnow',  blank = True)
    shoppingcart = models.ManyToManyField('CourseInstance', related_name='shoppingcart',  blank = True)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
    def get_shoppingcart(self):
        return ", ".join(shoppingcart.name for genre in self.shoppingcart.all()[:3])
    get_shoppingcart.short_description = "Shopping Cart"

    def get_coursestaken(self):
        return ", ".join(coursestaken.name for coursestaken in self.coursestaken.all()[:3])
    get_coursestaken.short_description = "Courses Taken"

    


class Days(models.Model):
    daysofweek = models.ManyToManyField("CourseInstance", related_name='daysofweek')
    OFFERED = (
            ("m", "Monday"),
            ("tu", "Tuesday"),
            ("w", "Wednesday"),
            ("th", "Thursday"),
            ("f", "Friday"),
    )

    daysoffered = models.CharField(
            max_length=2,
            choices=OFFERED,
            blank=True,
            default="m",
            help_text="Days offered",
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Reviews(models.Model):
    remarks = models.TextField(max_length=200)
    giver = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True)
