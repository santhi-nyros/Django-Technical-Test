#Django-Technical-Test

Please follow the below steps for setup the project

Clone or get code
--------------------
1. clone or download the code from git

Setup environment
--------------------
2. Create virtual environment by using below command
>virtualenv <env_name>

3.Activate your virtual environment.
> path_to_env/ source <env_name/bin/activate

4.Goto to project root folder and install packages in requirement.txt
> pip install -r requirement.txt or

  one by one
  pip install django
  so  on

Do db migrations and run the app
--------------------------------
5. Now do the db migrations

> python manage.py makemigrations

> python manage.py migrate

6. create a super user (for accessing through admin panel)
> python manage.py createsuperuser

>username:

>password:

7. Now run the app by using
> python manage.py runserver


