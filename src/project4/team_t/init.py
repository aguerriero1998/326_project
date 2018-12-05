import textwrap
from datetime import timedelta

# Create a super user to use the admin site.
from django.contrib.auth.models import User, Group
from faker import Faker
 
# Import our data model
from inspire.models import Course, CourseInstance, Professor, Student, Days, ProfessorReview, CourseReview

LEN = 20

fake = Faker()

days = []
for code in Days.OFFERED:
  day = day = Days(daysoffered=code[0])
  day.save() # saved the day 
  days.append(day)

#Fake Course Data w/ fake data
courses = []
classNames = [
    "CS 121",
    "CS 187",
    "CS 220",
    "CS 230",
    "CS 250",
    "CS 311",
    "CS 320",
    "CS 326",
]

genEds = [
    "AL",
    "AT",
    "BS",
    "HS",
    "U",
    "G",
    "R1",
    "R2",
    "PS",
    "SB",
]

descriptions = [
    "COMPSCI 121 provides an introduction to problem solving and computer programming using the programming language Java. The course teaches how real-world problems can be solved computationally using the object-oriented metaphor that underlies Java. Concepts and techniques covered include data types, expressions, objects, methods, top-down program design, program testing and debugging, state representation, interactive programs, data abstraction, conditionals, iteration, interfaces, inheritance, polymorphism, arrays, graphics, and GUIs. No previous programming experience is required; however, this course is intended for Computer Science majors or those who plan on applying to the major. Non-majors are strongly encouraged to take one of our programming courses designed for non-majors. Use of a laptop computer on which you can install software is required. Prerequisite: R1 (or a score of 20 or higher on the math placement test Part A), or one of the following courses: MATH 101&102 or MATH 104 or MATH 127 or MATH 128 or MATH 131 or MATH 132. 4 credits.",
    "The course introduces and develops methods for designing and implementing abstract data types using the Java programming language. The main focus is on how to build and encapsulate data objects and their associated operations. Specific topics include linked structures, recursive structures and algorithms, binary trees, balanced trees, and hash tables. These topics are fundamental to programming and are essential to other courses in computer science. The course involves weekly programming assignments, in-class quizzes, discussion section exercises, and multiple exams. Prerequisites: COMPSCI 121 (or equivalent Java experience). A grade of B or better in COMPSCI 121 (or a grade of C or better in COMPSCI 186 (or COMPSCI 190D) is required for students enrolling in COMPSCI 187 and Basic Math Skills (R1). Basic Java language concepts are introduced quickly; if unsure of background, contact instructor. 4 credits.",
    "Development of individual skills necessary for designing, implementing, testing and modifying larger programs, including: use of integrated design environments, design strategies and patterns, testing, working with large code bases and libraries, code refactoring, and use of debuggers and tools for version control. There will be significant programming and a mid-term and final examination. Prerequisite: COMPSCI 187. 4 credits.",
    "Large-scale software systems like Google - deployed over a world-wide network of hundreds of thousands of computers - have become a part of our lives. These are systems success stories - they are reliable, available () nearly all the time), handle an unbelievable amount of load from users around the world, yet provide virtually instantaneous results. On the other hand, many computer systems don't perform nearly as well as Google - hence the now-clich? In this class, we study the scientific principles behind the construction of high-performance, scalable systems. The course begins with a discussion of C language, and moves up the stack from there to the features of modern architectures, assembly languages, and operating system services such as I/O and synchronization. Prerequisites: COMPSCI 187. 4 credits.",
    "Lecture, discussion. Basic concepts of discrete mathematics useful to computer science: set theory, strings and formal languages, propositional and predicate calculus, relations and functions, basic number theory. Induction and recursion: interplay of inductive definition, inductive proof, and recursive algorithms. Graphs, trees, and search. Finite-state machines, regular languages, nondeterministic finite automata, Kleene's Theorem. Problem sets, 2 midterm exams, timed final. Prerequisite: MATH 132 and COMPSCI 187. 4 credits.",
    "This course will introduce you to algorithms in a variety of areas of interest, such as sorting, searching, string-processing, and graph algorithms. You will learn to study the performance of various algorithms within a formal, mathematical framework. You will also learn how to design very efficient algorithms for many kinds of problems. There will be one or more programming assignments as well to help you relate the empirical performance of an algorithm to theoretical predictions. Mathematical experience (as provided by COMPSCI 250) is required. You should also be able to program in Java, C, or some other closely related language. Prerequisite: COMPSCI 187 and either COMPSCI 250 or MATH 455. 4 credits.",
    "In this course, students learn and gain practical experience with software engineering principles and techniques. The practical experience centers on a semester-long team project in which a software development project is carried through all the stages of the software life cycle. Topics in this course include requirements analysis, specification, design, abstraction, programming style, testing, maintenance, communication, teamwork, and software project management. Particular emphasis is placed on communication and negotiation skills and on designing and developing maintainable software. Use of computer required. Several written assignments, in-class presentations, and a term project. This course satisfies the IE Requirement. Prerequisite: COMPSCI 220. 4 credits.",
    "The World Wide Web was proposed originally as a collection of static documents inter-connected by hyperlinks. Today, the web has grown into a rich platform, built on a variety of protocols, standards, and programming languages, that aims to replace many of the services traditionally provided by a desktop operating system. Topics will include: producing dynamic content using a server-based language, content serving databases and XML documents, session state management, multi-tier web-based architectures, web security, and core technologies including HTTP, HTML5, CSS, JavaScript, and SQL will be emphasized. This course will also study concepts and technologies including AJAX, social networking, mashups, JavaScript libraries (e.g., jQuery), and web security. This course is hands-on and project-based; students will construct a substantial dynamic web application based on the concepts, technologies, and techniques presented during lecture. This course satisfies the IE Requirement. Prerequisites: COMPSCI 220 or COMPSCI 230. 4 credits.",
]
for i in range(0,7):
    a_className = classNames[i]
    a_courseNumber = fake.random_int(70000,80000)
    a_description = descriptions[i]
    a_credits = fake.random_int(3,4)
    a_rating = fake.random_int(100, 500)/100
    a_gened = genEds[fake.random_int(0,9)]
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
location = ["Herter 102", "South College W245", "CS 151", "Hasbrouck 124","Herter 102", "South College W245", "CS 151", "Hasbrouck 124","Herter 102", "South College W245", "CS 151", "Hasbrouck 124","Herter 102", "South College W245", "CS 151", "Hasbrouck 124","Herter 102", "South College W245", "CS 151", "Hasbrouck 124",]
for i in range(0,20):
    a_name = courses[fake.random_int(0, len(courses) - 1)].name
    #TODO add in prof at the end
    a_classNumber = fake.random_int(1,1000)
    a_time = times[fake.random_int(0, len(times) - 1)]
    a_start = a_time[0]
    a_end = a_time[1]
    #TODO add in prerequisites at the end
    a_semester = "Spring"
    a_location = location[i]
    a_textbook = "TBD"
    a_available = 50


    courseInstance = CourseInstance(
                                    name = a_name,
                                    classnumber = a_classNumber,
                                    start = a_start,
                                    end = a_end,
                                    semester = a_semester,
                                    location = a_location,
                                    textbook = a_textbook,
                                    students = 0,
                                    available = a_available,
    )
    courseInstance.save()
    courseInstances.append(courseInstance)

#Professor portion of the data model w/ fake data
professors = []
professorNames = [
    "Neena Thota",
    "Gordon Anderson",
    "Rui Wang",
    "Eliot Moss",
    "Arjun Guha",
    "David Barrington",
    "Marius Minea",
    "Timothy Richards",    
]
for i in range(0,8):
    a_name = professorNames[i]
    professor = Professor(
                        name = a_name,
                        rating = fake.random_int(0,500)/100    
    )
    professor.save()
    professors.append(professor)


students = []
gender = ["male", "female"]
pronouns = ["he/him", "she/her"]

group = Group(name="Student")
group.save()

print("Listing Student User Login Info:")

for i in range(1,LEN):

    a_first_name = fake.first_name()
    a_last_name = fake.last_name()

    user = User.objects.create_user(a_first_name[0].lower() + a_last_name.lower(), a_first_name[0].lower() + a_last_name.lower() + "@326.umass.edu", a_last_name.lower())
    user.first_name = a_first_name
    user.last_name = a_last_name
    user.groups.add(group)
    user.save()
    
    print(f"Username: {a_first_name[0].lower() + a_last_name.lower()} Password: {a_last_name.lower()}")

    a_idnumber = fake.random_int(30000000,40000000)
    a_phonenumber = fake.phone_number()
    an_address = fake.address()
    a_gender = gender[fake.random_int(0,1)]
    a_pronouns = pronouns[fake.random_int(0,1)]
    a_emergency = fake.text(20)

    student = Student(
                        name = a_first_name + " " + a_last_name,
                        idnumber = a_idnumber,
                        phonenumber = a_phonenumber,
                        address = an_address,
                        gender = a_gender,
                        pronouns = a_pronouns,
                        emergency = a_emergency,
                        user = user
    )
    student.save()
    students.append(student)


professor_reviews = []
professor_review = [
    "Great professor",
    "Lots of homework",
    "Learned so much from them",
    "Exams are super hard",
    "Decent",
    "Do not buy the book, the professor has excellent slides",
    "Easy quizzes, if you do the reading",
    "You can tell they care about teaching",
    "The instructor was funny, knowledgeable, and willing to help students",
    "I liked the in-class demos/examples to help remember the material",
    "Pretty funny and tried to keep things interesting and he was very honest when we were going through slides that were boring",
    "They are absolutely awesome at teaching but sometimes the course matter seems a little bit rushed",
    "They were entertaining and engaged and they always communicated things in a clear way",
    "Brings enthusiasm and experience to every lecture",
    "I wish I could provide constructive criticism, but I can’t. Absolutely fantastic.",
    "I learned a great deal and exams were even challenging and fair to everyone.",                                    
]
for i in range(0,16):
    a_remarks = professor_review[i]

    review = ProfessorReview(remarks = a_remarks)

    review.giver = students[fake.random_int(0,len(students) - 1 )]
    review.professor = professors[fake.random_int(0,len(professors) - 1 )]

    review.save()
    professor_reviews.append(review)


for course in courses:
    for i in range(1, fake.random_int(2, 3)):
        course.recommendations.add(courseInstances[fake.random_int(0,len(courseInstances) - 1 )])
    course.save()



def get_course(courseInstance):
    global courses
    for course in courses:
        if course.name == courseInstance.name:
            print(f"course name : {course.name} courseInstance name : {courseInstance.name}")
            return course

for courseInstance in courseInstances:
    for day in days:
        num = fake.random_int(1,10)
        if(num < 5):
            courseInstance.days.add(day)

    if not courseInstance.days.count():
        courseInstance.days.add(days[2])

    course = get_course(courseInstance)
    print(course)
    print(courseInstance)
    courseInstance.basecourse = course
    courseInstance.credits = course.credits
    courseInstance.save()

    prof = professors[fake.random_int(0, len(professors) - 1 )]
    courseInstance.prof = prof
    courseInstance.save()

    for i in range(fake.random_int(0,2)): 
        courseInstance.prerequisites = courses[fake.random_int(0,len(courses) - 1 )]
        courseInstance.save()


    courseInstance.save()

for student in students:
    
    for i in range(1, fake.random_int(1, 10)):
        student.coursestaken.add(courseInstances[fake.random_int(0,len(courseInstances) - 1 )])
        student.save()

    for i in range(1, fake.random_int(2,5)):
        courseInstance = courseInstances[fake.random_int(0, len(courseInstances) - 1 )]
        if len(student.coursesnow.all().filter(start=courseInstance.start)) == 0:
            student.coursesnow.add(courseInstance)
            courseInstance.students += 1
            courseInstance.available -= 1
            courseInstance.save()

    for i in range(1, fake.random_int(1, 10)):
        student.shoppingcart.add(courseInstances[fake.random_int(0,len(courseInstances) - 1 )])
      
course_reviews = []
course_review = [
	"Good course, prepares you for the rest of the CS courses",
	"Interesting material, hard exams",
	"Long homeworks, but everything is graded fairly",
	"Really enjoyed the group aspect of this class",
	"Everyone should take this course. I learned so much",
	"By far my favorite class at UMASS. Would reccomend",
	"Avoid at all costs",
	"This class literally gave me nightmares",
	"This class was very alright",
	"Don't even bother going to class, just read the book",
	"One of the easiest classes, but not the most interesting",
	"I spent 6 years of my life on homework for this class",
	"The 5 multiple choice question online quizzes took me longer than 4 hours",
	"My favorite part about this course was when it was over",
	"Strong dislike",
	"Does not drip",
]
for i in range(0,16):
    a_remarks = course_review[i]

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
