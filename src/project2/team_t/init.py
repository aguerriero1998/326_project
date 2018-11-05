import textwrap
from datetime import timedelta

# Create a super user to use the admin site.
from django.contrib.auth.models import User
from faker import Faker
 
#Import our data model
from inspire.models import Course, CourseInstance, Professor, Student, Days, Reviews, CourseReview

LEN = 20

fake = Faker()

days = []
for code in Days.OFFERED:
  day = day = Days(daysoffered=code[0])
  day.save() # saved the day 
  days.append(day)

#Fake Course Data w/ fake data
courses = []
for i in range(1,5):
    a_className = fake.text(20)
    a_courseNumber = fake.random_int(70000,80000)
    a_description = fake.text(100)
    a_credits = fake.random_int(1,4)
    a_rating = fake.random_int(100, 500)/100
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
                    gened = a_gened,
                    major = a_major,
    )
    course.save()
    courses.append(course)
times = [("8:00", "9:30"), ("10:00","11:30"), ("12:00", "13:30"), ("14:00","15:30")]
#CourseInstances portion of the data model w/ fake data
courseInstances = []
for i in range(1,21):
    a_name = courses[fake.random_int(0, len(courses) - 1)].name
    #TODO add in prof at the end
    a_classNumber = fake.random_int(1,1000)
    a_time = times[fake.random_int(0, len(times) - 1)]
    a_start = a_time[0]
    a_end = a_time[1]
    #TODO add in prerequisites at the end
    a_semester = fake.text(6)
    a_location = fake.bothify(text="## ??", letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    a_textbook = fake.text(25)
    a_students = fake.random_int(0,500)
    a_available = 500 - a_students


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
    courseInstances.append(courseInstance)

#Professor portion of the data model w/ fake data
professors = []
for i in range(3,6):
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
for i in range(1,50):
    a_remarks = fake.text(200)

    review = Reviews(remarks = a_remarks)
    review.save()
    reviews.append(review)

for professor in professors:
    for i in range(1,fake.random_int(1, 4)):
        professor.review.add(reviews[fake.random_int(0,len(reviews) - 1 )])

for course in courses:
    course.reccomendation = courseInstances[fake.random_int(0, len(courseInstances) - 1 )]
    course.save()



def get_course(courseInstance, course):
    global courses
    for course in courses:
        if course.name == courseInstance.name:
            return course

for courseInstance in courseInstances:
    for day in days:
        num = fake.random_int(1,10)
        if(num < 5):
            courseInstance.days.add(day)

    if not courseInstance.days.count():
        courseInstance.days.add(days[2])

    course = get_course(courseInstance, course)
    courseInstance.course = course
    courseInstance.credits = course.credits
    courseInstance.save()

    prof = professors[fake.random_int(0, len(professors) - 1 )]
    courseInstance.prof = prof
    courseInstance.save()

    for i in range(fake.random_int(0,2)): 
        courseInstance.prerequisites = courses[fake.random_int(0,len(courses) - 1 )]
        courseInstance.save()


    courseInstance.basecourse = courses[fake.random_int(0,len(courses) - 1 )]
    courseInstance.save()

for student in students:
    
    for i in range(1, fake.random_int(1, 10)):
        student.coursestaken.add(courseInstances[fake.random_int(0,len(courseInstances) - 1 )])
        student.save()

    for i in range(1, fake.random_int(1,5)):
        courseInstance = courseInstances[fake.random_int(0, len(courseInstances) - 1 )]
        if len(student.coursesnow.all().filter(start=courseInstance.start)) == 0:
            student.coursesnow.add(courseInstance)

    for i in range(1, fake.random_int(1, 10)):
        student.shoppingcart.add(courseInstances[fake.random_int(0,len(courseInstances) - 1 )])
      
for review in reviews:
        review.giver = students[fake.random_int(0,len(students) - 1 )]
        review.save()

course_reviews = []
for i in range(1,50):
    a_remarks = fake.text(200)

    review = CourseReview(
        remarks = a_remarks,
    )
    review.giver = students[fake.random_int(0,len(students) - 1 )]
    review.course = courses[fake.random_int(0,len(courses) - 1 )]
    review.save()
    course_reviews.append(review)

username = "admin"
password = "admin"
email = "admin@326.edu"
adminuser = User.objects.create_user(username, email, password)
adminuser.save()
adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()
