import bcrypt
from datetime import datetime
from flask import jsonify, request
from flask_mongoengine import ValidationError
from models.user import User

def index():
  return jsonify({'message': 'This is an API endpoint'})

def post_signup():
    email = request.form.get('email')
    firstName = request.form.get('firstName')
    lastName = request.form.get('lastName')
    location = request.form.get('location')
    password = request.form.get('password')
    confirmPassword = request.form.get('confirmPassword')

    # Validate the incoming form data
    errors = []
    if not email or not email.strip():
        errors.append('You must provide an email in order to create an account')
    # Add other validation checks for firstName, lastName, location, password, confirmPassword...

    # Check if the email has already been registered
    existing_user = User.objects(email=email).first()
    if existing_user:
        errors.append('That email has already been taken, please try again')

    if errors:
        return jsonify(errors=errors, email=email, firstName=firstName, lastName=lastName, location=location), 400

    # If the form data is valid, create the new user
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    new_user = User(
        email=email,
        firstName=firstName,
        lastName=lastName,
        location=location,
        password=hashed_password,
        comments=[],
        joined=datetime.now(),
        popularity=0,
        posts=[],
        role='basic'
    )

    try:
        new_user.save()
        stripped_user_information = {
            'email': new_user.email,
            'firstName': new_user.firstName,
            'lastName': new_user.lastName,
        }
        return jsonify(
            message='We successfully uploaded your account to our database',
            strippedUserInformation=stripped_user_information
        )
    except ValidationError as e:
        return jsonify(message='Failed to save user', error=str(e)), 500
    except Exception as e:
        return jsonify(message='We were unable to upload your account to our database, please try again later', error=str(e)), 500