#!/usr/bin/env python3

from app import db
from models import Customer

if __name__ == '__main__':
    db.create_all()

    # Add sample customer data to the database
    customers_data = [
        {'name': 'Pop Smoke', 'email': 'popsmokedriller092@gmail.com', 'age': 30},
        {'name': 'Tupac Shakur', 'email': 'Tupacshakur254@gmail.com', 'age': 25},
        # Add more customer data here as needed
    ]

    for customer_data in customers_data:
        customer = Customer(**customer_data)
        db.session.add(customer)

    db.session.commit()

    print("Sample customer data added to the database.")


