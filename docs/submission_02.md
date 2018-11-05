Overview: Our application is called "Inspire". It is a new and improved version of spire. Our application makes a more user
friendly interface to shop for classes. We have a reccomendation section and rating of professors.

Team Members: Connor Reardon, Alex Guerriero, Chris Doan, Patrick Casey, Akshaya Bhattarai

Video Link:

Design Overview: For our database model we have courses, course instances, profesors, students, and days of the week.
The course class has information about the course such as course number, gen. ed. tag, and comments about the course.
The course instance class holds data having to do with specific offerings of the course such as when the ocurse is offered,
where the course is held, and the professor teaching the course. The professors class is used to store information about
professors like their name, previously taught courses, and reviews about their previous classes. The student class has
student information like their name, address, and emergency contact. The days class is used to represent which days of the week
course instance is offered. The reviews class has a review left by a student for a professor and a link to the student that gave the review. Course is connected to course instance which is connected to the rest of the models.

The URLS are mapped to the web pages that fit the needs of our application. The class-search and search-results html pages are mapped to paths that refer to the webpages. These are more general pages that contain forms (class-search) and the result of the search. The documentation tells us not to yet implement any forms, so to just view them we set a paths that display the templated files of our original mock ui's. The urls for shopping-cart, student-info, and dashboard all require an extra path that require the id of the student which act as a primary key. The professor contains a primary key of the professor name and the course info page contains the course id as the primary key in the url path. 

The VIEWS also reflect the functionality of the webpages we need. The class-search and search-result views are currently all hard-coded into the html templates as we have yet to do forms and filling in the forms to alter instances of a page. The student-info, professor-info, and course-info pages all use the Generic class's detail view. These web pages purely display the information included in the model representations for these entities so it was a deisgn choice to use the detail view. Dashboard will contain a copy of the student's schedule so we defined a get_list(day) function to assist in getting information for this schedule. The get_list(day) returns a list of dictionaries containing information like name of a couse, start and end times, and location from queried data from the course_instances model.

Problems/Successes: One problem we had was trying to represent the days of the week that a course is offered. We solved this by
making a separate days class which is linked to the course instance. The days class has choices of Monday-Friday that the course
can be available to take. Our teams communication and division of the work has been solid. We are all active on slack and met at the library on Sunday to get all of our parts of the projects synced up.

Another problem we ran into was design implementations for views.py. We had delegated the work for views.py and templating our mock ui HTML files into two seperate jobs. Because naming of variable contexts and whether to use generic views or to define contexts for views and templates are very closely related it require a lot of communication to complete. As a team the members who were assigned these tasked communicated well to finish and execute the project. Though we were succesful, maybe if we were to do it again, we would assign the job to the same individual.
