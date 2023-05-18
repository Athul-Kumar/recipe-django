from faker import Faker
fake = Faker()

import random
from .models import *


def seed_db(n=10) -> None:

    try:
        for _ in range(n):
            department_obj = Department.objects.all()
            random_index = random.randint(0, len(department_obj)-1)
            department = department_obj[random_index]
            student_id = f'STU-0{random.randint(50, 1000)}'
            student_name   = fake.name()
            student_age    = random.randint(18, 35)
            student_email   = fake.email()
            student_address  = fake.address()


            student_id_obj = StudentID.objects.create(student_id = student_id)

            student_obj = Student.objects.create(

                department = department,
                student_name = student_name,
                student_age = student_age,
                student_email = student_email,
                student_address = student_address,
                student_id  = student_id_obj,
           )

    except  Exception as e:
        print (e)




