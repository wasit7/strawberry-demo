# strawberry-demo

this repo for [strawberry-graphql-django](https://github.com/strawberry-graphql/strawberry-graphql-django) testing and demo


# create python environment

```sh
$conda create -n strawberry-demo python=3
$conda activate strawberry-demo
```

# create django project and app
```sh
$pip install django==3.2
$pip install Pillow
$django-admin startproject myproject
$cd myproject/
$python manage.py startapp myapp
$python manage.py makemigrations
$python manage.py migrate
$python manage.py createsuperuser
$python manage.py runserver
```