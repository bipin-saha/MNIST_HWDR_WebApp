# MNIST Handwritten Digit Recognition Web Application
This is a simple web application that recognizes handwritten digits using a pre-trained Convolutional Neural Network model. Users can upload an image of a handwritten digit, and the application will predict the digit and display the result.

## Table of Contents
### Installation
### Usage
### Model Training
### Folder Structure
### Technologies Used
### License

Installation
To run this web application locally, follow these steps:

Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/MNIST_HWDR_WebApp.git
Install the required dependencies. You can use a virtual environment to manage the dependencies:

bash
Copy code
cd MNIST_HWDR_WebApp
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
Download the pre-trained model checkpoint file (e.g., MNIST_HWDR_2D-feedforward.pth) and place it in the models folder.

Run the Flask application:

bash
Copy code
python app.py
Open a web browser and go to http://localhost:5000 to use the application.

Usage
Access the web application by visiting http://localhost:5000 in your web browser.

Click the "Choose File" button to upload an image containing a handwritten digit.

Click the "Predict" button to initiate the digit recognition process.

The predicted digit will be displayed on the web page along with the uploaded image.

You can upload more images to make additional predictions.

Model Training
If you want to train the MNIST digit recognition model yourself, you can follow these steps:

Make sure you have installed the required dependencies as mentioned in the installation section.

Open the train.py file in your code editor, and you can modify the training parameters if needed.

Run the training script:

bash
Copy code
python train.py
This will start the training process using the MNIST dataset and save the trained model checkpoint in the models folder.

You can then use the trained model checkpoint (MNIST_HWDR_2D-feedforward.pth) to replace the existing model checkpoint in the models folder for making predictions with the web application.

Folder Structure
MNIST_HWDR_WebApp/ - Root directory of the application.
app.py - The Flask web application script.
train.py - Script for training the model (if needed).
uploads/ - Folder where uploaded images are stored.
models/ - Folder for storing pre-trained model checkpoint files.
static/ - Folder for static assets (e.g., CSS, JavaScript).
templates/ - HTML templates for rendering web pages.
requirements.txt - List of Python dependencies.
Technologies Used
Python
Flask
PyTorch (for deep learning)
HTML/CSS
PIL (Python Imaging Library) for image processing
License
This project is licensed under the MIT License - see the LICENSE file for details.

