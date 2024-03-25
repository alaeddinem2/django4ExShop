import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from shop.models import Product, Category
from django.contrib.auth.models import User
import random
from faker import Faker




def seed_products(n):
    fake = Faker()
    
    

    for _ in range(n):
        images= ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg']
        # Create a new Post instance with the author
        Product.objects.create(
            category=Category.objects.get(id=random.randint(1,20)),
            name=fake.name(),
            image = f'products/{images[random.randint(0,9)]}',
            description=fake.text(max_nb_chars=100),
            price = round(random.uniform(20.99,99.99)),
        )

    print(f'Seeded {n} products')

def seed_categories(n):
    fake = Faker()
    
    

    for _ in range(n):

        Category.objects.create(
            name=fake.name(),
            
        )

    print(f'Seeded {n} products')


# Example usage: seed 10 posts
#seed_Post(35)

#seed_categories(10)

seed_products(100)