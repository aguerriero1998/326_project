import textwrap
from datetime import timedelta

# Create a super user to use the admin site.
from django.contrib.auth.models import User
from faker import Faker
 
#Import our data model
from inspire.models import Course, CourseInstance, Professor, Student, Days, Reviews

LEN = 20

fake = Faker()

#Fake Course Data w/ fake data
courses = []
for i in range(1,LEN):
    a_className = fake.text(20)
    a_courseNumber = fake.random_int(70000,80000)
    a_description = fake.text(100)
    a_credits = fake.random_int(1,4)
    a_rating = fake.random_int(100, 500)/100
    a_comments = fake.text(100)
    a_gened = fake.text(5)
    a_major = fake.text(25)
    #add in later?
    #a_recommendation = 

    #Makes the new fake Course object
    course = Course(name = a_className,
                    coursenumber = a_courseNumber,
                    description = a_description,
                    credits = a_credits,
                    rating = a_rating,
                    comments = a_comments,
                    gened = a_gened,
                    major = a_major,
    )
    course.save()
    courses.append(course)

#CourseInstances portion of the data model w/ fake data
courseInstances = []
for i in range(1,LEN):
    a_name = fake.text(20)
    #TODO add in prof at the end
    a_classNumber = fake.random_int(70000,80000)
    a_start = fake.time(pattern="%H:%M", end_datetime=None)
    a_end = fake.time(pattern="%H:%M", end_datetime=None)
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
                                    name = a_name,
                                    classnumber = a_classNumber,
                                    start = a_start,
                                    end = a_end,
                                    semester = a_semester,
                                    location = a_location,
                                    textbook = a_textbook,
                                    students = a_students,
                                    available = a_available,
    )
    courseInstance.save()
    #courseInstance.days.add(a_days)
    #courseInstance.studentname.add(a_studentname)

    #courseInstance.save()
    courseInstances.append(courseInstance)

#Professor portion of the data model w/ fake data
professors = []
for i in range(1,LEN):
    a_name = fake.name()
    professor = Professor(
                        name = a_name,
                        rating = fake.random_int(0,500)/100    
    )
    professor.save()
    professors.append(professor)


students = []
gender = ["male", "female"]
pronouns = ["he/him", "she/her"]
for i in range(1,LEN):
    a_name = fake.name()
    a_idnumber = fake.random_int(30000000,40000000)
    a_email = fake.email()
    a_phonenumber = fake.phone_number()
    a_gender = gender[fake.random_int(0,1)]
    a_pronouns = pronouns[fake.random_int(0,1)]
    a_emergency = fake.text(20)

    student = Student(
                        name = a_name,
                        idnumber = a_idnumber,
                        email = a_email,
                        phonenumber = a_phonenumber,
                        gender = a_gender,
                        pronouns = a_pronouns,
                        emergency = a_emergency,
    )
    student.save()
    students.append(student)


reviews = []
for i in range(1,LEN):
    a_remarks = fake.text(200)

    review = Reviews(remarks = a_remarks)
    review.save()
    reviews.append(review)

for professor in professors:
    for i in range(1,fake.random_int(1, 4)):
        professor.review.add(reviews[fake.random_int(0,len(reviews) - 1 )])
    for i in range(1, fake.random_int(1, 3)):
        professor.taught = courseInstances[fake.random_int(0,len(courseInstances) - 1 )]
        professor.save()

for course in courses:
    for i in range(1, fake.random_int(1, 3)):
        course.reccomendation = courseInstances[fake.random_int(0,len(courseInstances) - 1 )]
        course.save()

for courseInstance in courseInstances:
    for i in range(1, fake.random_int(1, 3)):
        day = Days.OFFERED[fake.random_int(0, 4)]
        day = Days(daysoffered = day[0])
        day.save() # saved the day 
        courseInstance.days.add(day)

    courseInstance.course = courses[fake.random_int(0,len(courses) - 1 )]
    courseInstance.save()

    courseInstance.course = professors[fake.random_int(0,len(professors) - 1 )]
    courseInstance.save()

    for i in range(fake.random_int(0,2)): 
        courseInstance.course = courses[fake.random_int(0,len(courses) - 1 )]
        courseInstance.save()

for student in students:
    
    for i in range(1, fake.random_int(1, 10)):
        student.coursestaken = courses[fake.random_int(0,len(courses) - 1 )]
        student.save()

    for i in range(1, fake.random_int(1,5)):
        student.coursesnow.add(courseInstances[fake.random_int(0,len(courseInstances) - 1 )])
    for i in range(1, fake.random_int(1, 10)):
        student.shoppingcart = courseInstances[fake.random_int(0,len(courseInstances) - 1 )]
        student.save()

for review in reviews:
        review.giver = students[fake.random_int(0,len(students) - 1 )]
        review.save()


username = "admin"
password = "admin"
email = "admin@326.edu"
adminuser = User.objects.create_user(username, email, password)
adminuser.save()
adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()
