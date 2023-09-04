import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


from faker import Faker
import random
from products.models import Products


def seed_product(n):
    fake = Faker()
    images = ['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png']
    
    for x in range(n):
        Products.objects.create(
            name = fake.name(),
            price = round(random.uniform(200.99 , 999.99),2),
            image = f'products/{images[random.randint(0,5)]}'
        )
    print(f'{n} products was successfuly')



seed_product(75)