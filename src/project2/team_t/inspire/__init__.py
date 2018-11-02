import textwrap
from datetime import timedelta

# Create a super user to use the admin site.
from django.contrib.auth.models import User
from faker import Faker
import random
 
#Import our data model
from inspire.models import Course, CourseInstance, Professor, Student

fake = Faker()

#Fake Course Data
courses = []
for i in range(1,50):
    a_className = fake.text(20)
    a_courseNumber = fake.random_int(70000,80000)
    a_description = fake.text(100)
    a_credits = fake.random_int(1,4)
    a_rating = random.randint(100, 500)/100
    a_comments = fake.text(100)
    a_gened = fake.text(3)
    a_major = fake.text(25)
    #figure out later
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
                    recomendation = a_recommendation
    )
    
    course.save()
    courses.append(course)

courseInstances = []
for i in range(1,50):
    a_name = fake.text(20)
    prof =


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