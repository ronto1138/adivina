import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','adivina.settings')

import django
django.setup()

import random

from usrcontrol.models import User
from faker import Faker


fakegen = Faker()


def populate(N=5):
    for entry in range(N):
        
        #Create the fake data for that entry
        fake_nombre = fakegen.name().split()
        primera = list(fake_nombre[0])
        segunda = list(fake_nombre[1])
        fake_iniciales = primera[0]+segunda[0]
        intentos = random.randint(5,15)
        
        # Create the new webpage entry
        usr = User.objects.get_or_create(iniciales=fake_iniciales,intentos=intentos)[0]
        
if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("Population completed!")