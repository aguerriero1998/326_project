Title: Team tEaM

Subtitle: Inspire

Semester: Fall 2018

Overview: Inspire is a web application modeled after Spire. With inspire, you will get the full Spire experience with a more intuitive and user friendly experience. Inspire allows students to leave course reviews and professor reviews once they have taken a class. 

Team Members: Akshaya Bhattarai,
Alex Guerriero,
Christopher Doan,
Connor Reardon,
Patrick Casey 

User Interface:<br/> Login View - allows Users to login or get to password reset

![example image](final_imgs/login.png)

Forgot Password View- allows User to be sent password reset

![example image](final_imgs/password.png)

Schedule View- acts as a homepage/index for Student Users and shows a schedule based on Student's classes

![example image](final_imgs/schedule.png)

Student Info View- Shows relevant info about student like phone number, address, and courses taken. Has links to edit info, add course reviews, and add professor reviews

![example image](final_imgs/studentinfo.png)

Edit Info View- allows student to edit their phone number, address, emergency contact, pronouns and gender through forms

![example image](final_imgs/editstudent.png)

Shopping Cart View- view to show current shopping cart and currently enrolled classes- able to enroll in classes from shopping cart.

![example image](final_imgs/shoppingcart.png)

Class Search View- view for student Users to look up classes using a keyword.

![example image](final_imgs/classsearch.png)

Search Result View- view that show relevant courses from class search page. Shows relevant info like professor, time, and location.

![example image](final_imgs/searchresults.png)

Add Course Review View- allows students to add course reviews for courses they have previously taken

![example image](final_imgs/coursereview.png)

Add Professor Review View- allows students to add professor reviews for professors they have had for previously taken classes.

![example image](final_imgs/profreview.png)

 Course List View- view to show directory of all courses
 
![example image](final_imgs/courselist.png)
 
 Add Course View- only accessible by admin/professor Users. allows for courses to be added.
 
![example image](final_imgs/addcourse.png)

Course Info View- shows a course's info including description, credits, and reviews.

![example image](final_imgs/courseinfo.png)

Course Instance List- shows a list of the currenty course instances offered the semester.

![example image](final_imgs/instancelist.png)

Course Instance Info- shows info on course instance - incuding enrollment, professor, time, location.

![example image](final_imgs/instanceinfo.png)
 
 

Data Model: 
![example image](final_imgs/datamodel.png)

In our data model we have students, professors, courses, course instances, course reviews, professor reviews, and days of the week. Students are the students at UMass. Courses are the courses offered at UMass. Course instances are what students enroll in for each semester. Professors are the people who are teaching the course for the semester. Course and professor reviews are remarks left by students about their courses and professors. Days of the week are days in which a course instance is held. Courses are connected to a course instance and course reviews. Course instances are connected to the students taking that instance and the professor teaching that instance. Days of the week the course instance is offered is also connected to course instance. The professor is connected to their reviews. Lastly, all of the reviews are connected to a student who wrote the reviews.


URL Routes/Mappings:

|                Path                |                                                                  Description                                                                 |
|:----------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------:|
| accounts/login                     | When user is not logged-in this is the first url they see. Login required to access app                                                      |
| accounts/password_reset            | From the login page- if a user forgets password they can go to this page.                                                                    |
| accounts/logout                    | From any page in the app, a user can logout to get to this page. Shows they are logged out                                                   |
| inspire/<int:pk>                   | Default homepage for student User after login                                                                                                |
| inspire/class-search               | Sidebar component that is used to start class searches- accessible by all Users                                                              |
| inspire/search-results             | Accessed from class-search to show search results- accessible by all Users                                                                   |
| inspire/students                   | Sidebar component and shows list of all students- accessible by admins Users only                                                            |
| inspire/courses                    | Sidebar component shows courses- accessible by all Users                                                                                     |
| inspire/course-instances           | Sidebar component shows course instances- accessible by all Users                                                                            |
| inspire/course/<int:pk>            | Routed from courses list- shows info on the course indicated by its pk course number. Accessible by all Users                                |
| inspire/course-instance/<int:pk>   | Routed from course instances list- shows info on course instance indicated by its pk class number. accessible from all Users                 |
| inspire/course-review/<int:pk>     | Routed from student info page - adds a review for course by its pk course number. Accessible by student Users                                |
| inspire/course-review/success      | Routed from course-review - shows successful review added. Accessible by student Users                                                       |
| inspire/professors                 | Sidebar component shows list of professors - accessible by all Users                                                                         |
| inspire/professor/<str:pk>         | Routed from professors list- shows information on professor. Accessible by all Users                                                         |
| inspire/professor/<str:pk>/review  | Routed from student info page- adds a review for professor by their name. Accessible by student Users                                        |
| inspire/professor/<str:pk>/success | Routed from professor review page- shows successful review added. Accessible by student Users                                                |
| inspire/shopping-cart/<int:pk>     | Sidebar component- shows unique shopping cart to student identified by their pk id number. Accessible by single student User                 |
| inspire/student-info/<int:pk>      | Sidebar component- shows unique student info page for student identified by their pk id number. Accessible by single student and admin Users |
| inspire/student-info/<int:pk>/edit | Accessed from student info page - able to edit info on student. Accessed by single student and admins.                                       |
| inspire/friends/<int:pk>           | Accessed from student info page- shows friends of student. Accessed by single student and admin Users                                        |
| inspire/register                   | Accessed from the login page - allows someone to create a new student 
                                                       

Authentication/Authorization: A final up-to-date description of how users are authenticated and any permissions for specific users (if any) that you used in your application. You should mention how they relate to which UI views are accessible.

Team Choice: Our team choice addition was to deploy our application to a server. Our website has the domain www.spire-is-bad.com is accessible on the internet. To accommodate for this we added a url and view to register a user. We additionally had to obtain a domain name and correctly set up DNS records so that our application is able to be accessed at the domain.

You should briefly mention your team choice component for your application. You should highlight any additions to your application that are part of your team choice, such as, URL routes, UI views, data model, to make it clear what your team choice addition is. 

Conclusion: A conclusion describing your team’s experience in working on this project. This should include what you learned through the design and implementation process, the difficulties you encountered, what your team would have liked to know before starting the project that would have helped you later, and any other technical hurdles that your team encountered.
