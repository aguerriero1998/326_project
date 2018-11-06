In this project, my main focus was working on populating our data model with fake data.
To accomplish this I used the Faker library to fill our database with fake data that could
be dispalyed by the front end of the application.

The main issue when working with the Faker library was filling in ManyToMany and Foreign key fields as it was not possible to fill these in directly. It took a bit of research and creativity, but eventually the database began to populate properly. Another issue that we had was running init.py from the terminal. To get around this issue and to standardize our initialization process, I wrote a shell file called init.sh that initializes the project properly.

Lastly I continually edited our data model as we discovered issues with it during development. Several fields were added and deleted from the model and some fields were changed. For example a Foreign Key was converted to  a ManyToMany field as it became apparent that a ForeignKey was not servicing our needs properly.
