'''
Create a script that creates fake data for an ecommerce store
- customers 
- products 
- orders
- order items

'''
from faker import Faker
import uuid
import random
import json
fake = Faker()

def create_customers(num_cust):
    customer_list =  []

    for num in range(num_cust):

        customer_list.append({"customer_id": fake.uuid4(),  # unique ID
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "phone_number": fake.phone_number(),
            "gender": random.choice(["Male", "Female", "Other"]),
            "birthdate": fake.date_of_birth(minimum_age=18, maximum_age=80).isoformat(),
            "signup_date": fake.date_between(start_date="-5y", end_date="today").isoformat(),
            "last_login": fake.date_time_between(start_date="-1y", end_date="now").isoformat(),
            "loyalty_member": fake.boolean(chance_of_getting_true=40), 
            "loyalty_points": random.randint(0, 5000),
            "street_address": fake.street_address(),
            "city": fake.city(),
            "state": fake.state_abbr(),
            "country": fake.country(),
            "zip_code": fake.zipcode()})
    
    return (customer_list)

def create_products(num_products):
    product_list = []

    for num in range(num_products):
        product_list.append({})