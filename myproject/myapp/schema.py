# schema.py
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