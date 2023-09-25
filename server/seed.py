#!/usr/bin/env python3

from app import db
from models import Customer

if __name__ == '__main__':
    db.create_all()

    # Add sample customer data to the database
    customers_data = [
        {'name': 'John Doe', 'email': 'john@example.com', 'age': 30},
        {'name': 'Jane Smith', 'email': 'jane@example.com', 'age': 25},
        # Add more customer data here as needed
    ]

    for customer_data in customers_data:
        customer = Customer(**customer_data)
        db.session.add(customer)

    db.session.commit()

    print("Sample customer data added to the database.")

            age= randint(0, 125),
            name=fake.name()
        )
        customers.append(customer)

    db.session.add_all(customers)
    db.session.commit()        

if __name__ == '__main__':
    with app.app_context():
        make_customers()
