from distutils.log import debug
from flask import Flask, request, jsonify, make_response
from flask_migrate import Migrate
from models import Customer, db
from flask_cors import CORS  # Add CORS for cross-origin requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app, db)

db.init_app(app)

@app.route("/customers", methods=['GET', 'POST'])
def customers():
    if request.method == 'GET':
        return make_response(jsonify([customer.to_dict() for customer in Customer.query.all()]))

    if request.method == 'POST':
        data = request.get_json()

        # Form validation using Yup-like schema
        schema = {
            'name': str,  # Example validation for a string
            'email': str,
            'age': int,
        }

        # Validate the form data
        for key, value in schema.items():
            if key not in data:
                return make_response(jsonify({'error': f'Missing field: {key}'}), 400)
            if not isinstance(data[key], value):
                return make_response(jsonify({'error': f'Invalid type for field {key}'}), 400)

        customer = Customer(name=data['name'], email=data['email'], age=data['age'])
        db.session.add(customer)
        db.session.commit()
        return make_response(
            jsonify(
                {'id': customer.id, 'name': customer.name, 'email': customer.email, 'age': customer.age}),
            201)

if __name__ == "__main__":
    app.run(port="5555", debug=True)

