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

ADD INFO ABOUT URLS AND VIEWS HERE

Problems/Successes: One problem we had was trying to represent the days of the week that a course is offered. We solved this by
making a separate days class which is linked to the course instance. The days class has choices of Monday-Friday that the course
can be available to take. Our teams communication and division of the work has been solid. We are all active on slack and met at the library on Sunday to get all of our parts of the projects synced up.

ADD SOME OF YOUR SUCCESSES/PROBLEMS HERE
