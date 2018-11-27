Overview: Our application is called "Inspire". It is a new and improved version of spire. Our application makes a more user
friendly interface to shop for classes. We have a reccomendation section and rating of professors. In this project submission, we have added user authentication and interaction. This means our new homepage after log-in is of a student's current schedule. Many forms we did not have working prior are also updated and working.

Team Members: Connor Reardon, Alex Guerriero, Chris Doan, Patrick Casey, Akshaya Bhattarai

Video Link: https://youtu.be/qLiF2cqTZdA

Design Overview: -no login info yet/authentication yet-
In this submission we added a few forms to update and create information about for the database. We have created a three forms that are found on the student info page. We have a edit info form. This gives the students the ability to change their own info from the database including things like address, phone number, pronouns, and emergency contact. The form has the character limit for its respective fields and will not update otherwise. The other two forms are concerning professors and courses. The student info displays information about a student's taken courses and the professor that taught the course. The student is able to leave a review about the course and the professor. This creates a review that is attached the course and professor in the database.
Another form created for the webapp is something that is for the admin/professor side of things. It is a form to add a course to the webapp. The admin will have to include things like the course name, the number of credits, its desciption and subject. This creates something for the database on the admin side of authentication.
Also, added a way for a password to be reset via locally sent emails.

Problems/Successes: A problem we ran into was for adding reviews, we needed to know which student added the review but did not want a student to enter their own student id when adding a review (its a little redundant since the page is only accessible if they take the class and are logged in) We solved this by creating a hidden input field that we autofill with their student id.

Team Choice: Implement a course recommendation feature. This will curate a student's taken courses and the recommendations of other students for these courses to show courses that the student would be interested in, or would be the be the logical next step in the courses they are taking. This is based off of recommendations created by users. 
