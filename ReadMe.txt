# create a virtual enviroment
> python -m venv env
# active venv
# on linux :
> source env/bin/activate
#on windows : 
> env/script/activate
# install requirements
> pip install -r requirements.txt
# create database
> python manage.py migrate
#runserver
> python manage.py runserver
