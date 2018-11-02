import textwrap
from datetime import timedelta

# Create a super user to use the admin site.
from django.contrib.auth.models import User
from faker import Faker
 
#Import our data model
from inspire.models import Course, CourseInstance, Professor, Student

fake = Faker()

#Fake Course Data w/ fake data
#TODO add in recommendation at the end!!!
courses = []
for i in range(1,20):
    a_className = fake.text(20)
    a_courseNumber = fake.random_int(70000,80000)
    a_description = fake.text(100)
    a_credits = fake.random_int(1,4)
    a_rating = fake.random_int(100, 500)/100
    a_comments = fake.text(100)
    a_gened = fake.text(3)
    a_major = fake.text(25)
    #add in later?
    #a_recommendation = 

    #Makes the new fake Course object
    course = Course(name = a_className,
                    courseNumber = a_courseNumber
                    description = a_description
                    credits = a_credits
                    rating = a_rating
                    comments = a_comments
                    gened = a_gened
                    major = a_major
    )
    course.save()
    courses.append(course)

#CourseInstances portion of the data model w/ fake data
courseInstances = []
for i in range(1,20):
    a_name = fake.text(20)
    #TODO add in prof at the end!!!!!
    a_classNumber = fake.random_int(70000,80000)
    a_time = fake.time(pattern="%H:%M", end_datetime=None)
    #TODO add in prerequisites at the end
    a_semester = fake.text(6)
    a_location = fake.bothify(text="## ??", letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    a_textbook = fake.text(25)
    a_students = fake.random_int(0,500)
    a_available = 500 - a_students
    #TODO figure out multiple days of the week?
    a_days = fake.day_of_week()
    a_studentname = fake.name()
    #TODO implement courses taken later?

    courseInstance = CourseInstance(
                                    name = a_name
                                    classnumber = a_classNumber
                                    time = a_time
                                    semester = a_semester
                                    location = a_location
                                    textbook = a_textbook
                                    students = a_students
                                    available = a_available
                                    days = a_days
                                    studentname = a_studentname
    )
    courseInstance.save()
    courseInstances.append(CourseInstance)

#Professor portion of the data model w/ fake data
professors = []
for i in range(1,20):
    a_name = fake.name()
    #TODO implement courses taught later
    a_review = fake.text(100)

    professor = Professor(
                        name = a_name
                        review = a_review
    )
    professor.save()
    professors.append(professor)


students = []
gender = ["male", "female"]
pronouns = ["he/him", "she/her"]
for i in range(1,20):
    a_name = fake.name()
    a_idnumber = fake.random_int(30000000,40000000)
    a_email = fake.email()
    a_phonenumber = fake.phone_number()
    a_gender = gender[fake.random_int(0,1)]
    a_pronouns = pronouns[fake.random_int(0,1)]
    a_emergency = fake.text(20)
    #TODO figure out coursesTaken and shoppingCart
    a_coursesNow = courseInstances[fake.random_int(0,19)]



username = "admin"
password = "admin"
email = "admin@326.edu"
adminuser = User.objects.create_user(username, email, password)
adminuser.save()
adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()
message = f"""
====================================================================
The database has been setup with the following credentials:
  username: {username}
  password: {password}
  email: {email}
You will need to use the username {username} and password {password}
to login to the administrative webapp in Django.
Please visit http://localhost:8080/admin to login to the admin app.
Run the django server with:
  $ python3 manage.py runserver 0.0.0.0:8080"
====================================================================
"""
print(message)