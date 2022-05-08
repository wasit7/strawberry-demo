# types.py
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
    name: str
    color: str