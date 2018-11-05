rm -f db.sqlite3 
python3 manage.py makemigrations
python3 manage.py migrate --run-syncdb
python3 manage.py shell < init.py
