line command
python manage.py migrate
python manage.py runserver


git init
git add .
git commit -m 'xxx'
git status
git push heroku master
heroku ps:scale web=1
heroku open
heroku run python manage.py migrate
