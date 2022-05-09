# strawberry-demo

this repo for [strawberry-graphql-django](https://github.com/strawberry-graphql/strawberry-graphql-django) testing and demo


# create python environment

```sh
$conda create -n strawberry-demo python=3.10.4
$conda activate strawberry-demo
```

# create django project and app
```sh
$pip install django==3.2
$pip install PillowPillow==9.1.0
$pip install strawberry-graphql-django==0.2.5
$django-admin startproject myproject
$cd myproject/
$python manage.py startapp myapp
$python manage.py makemigrations
$python manage.py migrate
$python manage.py createsuperuser
$python manage.py runserver
```
# models.py
```python
# /myapp/models.py
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=5)
    email = models.EmailField()

class Item(models.Model):
    UNIT_NAME_CHOICE = [ ("ชิ้น","ชิ้น"),("กร้ม","กร้ม") ]
    title = models.CharField(max_length=100)
    unit = models.CharField(max_length=5, choices=UNIT_NAME_CHOICE, default="ชิ้น")
    unit_price = models.DecimalField(max_digits=5, decimal_places=2) #999.99
    image = models.ImageField(upload_to='myimages') #from week05
    description = models.CharField(max_length=100, null=True, blank=True)

class OrderItem(models.Model):
    profile = models.ForeignKey( Profile, on_delete=models.CASCADE)
    item = models.ForeignKey( Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

class Fruit(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
```

# add types.py
```python
# /myapp/types.py
import strawberry_django
from . import models
from strawberry_django import auto
from typing import List

@strawberry_django.type(models.Profile)
class Profile:
    id: auto
    user: auto
    name: auto
    address: auto
    postcode: auto
    email: auto

@strawberry_django.type(models.Item)
class Item:
    title: auto
    unit: auto
    unit_price: auto
    image: auto
    description: auto

@strawberry_django.type(models.OrderItem)
class OrderItem:
    profile: 'Profile'
    item: 'Item'
    quantity: auto

@strawberry_django.type(models.Fruit)
class Fruit:
    id: auto
    name: str
    color: str
```

# add shema.py
```python
# /myapp/schema.py
import strawberry
import strawberry_django
from typing import List
from .types import Profile, Item, OrderItem, Fruit

@strawberry.type
class Query:
    profiles: List[Profile] = strawberry_django.field()
    items: List[Item] = strawberry_django.field()
    orderitems: List[OrderItem] = strawberry_django.field()
    
    fruit: Fruit = strawberry_django.field()
    fruits: List[Fruit] = strawberry_django.field()

schema = strawberry.Schema(query=Query)
```

# add urls.py
```python
# /myapp/urls.py
from django.urls import include, path
from strawberry.django.views import AsyncGraphQLView
from .schema import schema

urlpatterns = [
    path('graphql', AsyncGraphQLView.as_view(schema=schema)),
]
```