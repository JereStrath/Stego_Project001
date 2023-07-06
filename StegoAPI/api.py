from flask import Flask, request, jsonify, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from keras.models import load_model
import numpy as np
from os import path
import os
import tensorflow as tf
from PIL import Image
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hjshjhdjahkjshkjdhjs'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Replace with your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Load the stegomalware detection model
model = load_model('modelfinal.h5')

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the main page
@app.route('/', methods=['GET'])
def index():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return redirect(url_for('login'))

# Route for the image detection
@app.route('/detect', methods=['POST'])
def detect():
    if 'username' in session:
        try:
            # Get the uploaded image file
            image_file = request.files['image']

            # Save the image file to a temporary location
            image_path = 'temp_image.jpg'
            image_file.save(image_path)

            # Perform detection and classification using the loaded model
            result = perform_detection(image_path)

            # Delete the temporary image file
            os.remove(image_path)

            # Return the prediction result as JSON
            return jsonify(result)
        except Exception as e:
            return jsonify({'error': str(e)})
    else:
        return jsonify({'error': 'You must log in to perform detection.'})

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username exists in the database
        with app.app_context():
            user = User.query.filter_by(username=username).first()
        if user:
            # Check if the entered password matches the stored password
            if hashlib.sha256(password.encode()).hexdigest() == user.password:
                session['username'] = username
                return redirect(url_for('index'))

        return render_template('login.html', error='Invalid username or password.')

    return render_template('login.html')

# Route for the logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Route for the signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if 'username' in session:
        return redirect(url_for('index'))
    elif request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        # Check if the username already exists in the database
        with app.app_context():
            user = User.query.filter((User.username == username) | (User.email == email)).first()
        if user:
            return render_template('signup.html', error='Username or email already exists.')

        # Create a new user in the database
        new_user = User(email=email, username=username, password=hashlib.sha256(password.encode()).hexdigest())
        with app.app_context():
            db.session.add(new_user)
            db.session.commit()

        return redirect(url_for('login'))

    return render_template('signup.html')

def perform_detection(image_path):
    # Preprocess the image (you may need to resize, normalize, etc.)
    image = preprocess_image(image_path)
    # Perform prediction using the loaded model
    prediction = model.predict(image)

    # Process the prediction result
    is_stegomalware = prediction > 0.5

    return {'prediction': float(prediction), 'is_stegomalware': bool(is_stegomalware)}

def preprocess_image(image_path):
    # Your preprocessing code here
    image = Image.open(image_path)
    target_size = (256, 256)  # Replace with the target input size of your model
    image = image.resize(target_size)
    image = image.convert('RGB')
    image_array = np.array(image)
    image_array = image_array.astype(np.float32) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

if __name__ == '__main__':
    app.run(debug=True)
