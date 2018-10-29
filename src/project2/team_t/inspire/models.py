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
    reccomendation =  models.ForeignKey('CourseInstance', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class CourseInstance(models.Model):

    name = models.CharField(max_length=20, help_text='Enter a class name')
    prof = models.ForeignKey('Professor', on_delete=models.SET_NULL, null=True)
    classnumber = models.IntegerField(validators=[MaxValueValidator(1000), MinValueValidator(1)])
    time = models.TimeField(null=True, blank=True)
    prerequisites = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
    semester = models.CharField(max_length=6)
    location = models.CharField(max_length=25)
    textbook = models.CharField(max_length=25)
    students = models.IntegerField(validators=[MaxValueValidator(500), MinValueValidator(0)])
    available = models.IntegerField(validators=[MaxValueValidator(500), MinValueValidator(0)])
    days = ArrayField(models.CharFIeld(max_length=15),size=7)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Professor(models.Model):
    name = models.CharField(max_length=20, help_text='Enter a name')
    taught = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
    review = models.TextField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=25)
    idnumber = models.IntegerField(validators=[MaxValueValidator(40000000), MinValueValidator(30000000)])
    email = models.EmailField(max_length=25)
    gender = models.CharField(max_length=25)
    pronouns = models.CharField(max_length=25)
    emergency = models.CharField(max_length=25)
    coursestaken = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name




