rm -f db.sqlite3 
pip3 install django-widget-tweaks
python3 manage.py makemigrations
python3 manage.py migrate --run-syncdb
python3 manage.py shell < init.py
