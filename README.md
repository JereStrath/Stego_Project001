# Stegomalware Detection System

This project is divided into two parts:
1. Making the Detection Model
2. Making the detection system

# 1. Model crreation part

## Image Classification with TensorFlow

This repository contains code for performing image classification using TensorFlow and Keras. The code is organized into several sections, each serving a specific purpose. Below is an overview of the code functionality:

## Setup

- Required libraries: TensorFlow, OpenCV, Matplotlib, and NumPy.
- CPU configuration for TensorFlow.

## Dataset Preparation

- The dataset is assumed to be located in the `train` directory.
- You can find the dataset using the link below:
  ``` bash
  https://www.kaggle.com/datasets/marcozuppelli/stegoimagesdataset
- Supported image file extensions: jpeg, jpg, bmp, and png.
- Images and labels are loaded, preprocessed, and stored in separate lists.
- Batch processing is performed with further preprocessing (e.g., normalization, one-hot encoding).

## Image Dataset Creation

- The `image_dataset_from_directory` function is used to create an image dataset.
- Images are resized and preprocessed (scaling pixel values to [0, 1]).
- The dataset is split into training, validation, and testing sets.

## Model Creation and Training

- A Convolutional Neural Network (CNN) model is constructed using Keras.
- The model architecture consists of multiple convolutional and dense layers.
- The model is compiled with the Adam optimizer, binary cross-entropy loss, and accuracy metric.
- Training is performed using the training and validation sets.
- Training progress is logged using a TensorBoard callback.
- Training loss and accuracy history are visualized using Matplotlib.

## Model Evaluation

- The trained model is evaluated on the test set.
- Precision, recall, and accuracy metrics are calculated.

## Model Usage and Saving

- The model is saved to a file (`model/modelfinal.h5`) for future use.
- A sample image is loaded and preprocessed for prediction.
- The saved model is loaded and used to predict the class of the sample image.

## Additional Image Loading and Preprocessing

- An alternative method for loading and preprocessing images using PIL and NumPy is provided.

Please note that the code provided is a combination of different parts, and some sections might not fit together properly. Feel free to adapt and modify the code as needed for your specific use case.

For detailed implementation and usage instructions, please refer to the code comments and documentation.


# 2. Making of the Detection System

The Stegomalware Detection System is an application that uses machine learning techniques to detect the presence of stegomalware in images. It allows users to upload suspicious images and performs a prediction on whether the image contains stegomalware or not.

## Features

- User authentication: Users can create an account, log in, and log out to access the system.
- Image upload: Users can upload suspicious images for stegomalware detection.
- Prediction: The system uses a trained machine learning model to predict whether the uploaded image contains stegomalware.
- User-friendly interface: The web-based user interface provides an intuitive and interactive experience for users.

## Technologies Used

- Python
- Flask (web framework)
- TensorFlow (machine learning framework)
- OpenCV (image processing library)
- SQLite (database)
- HTML/CSS/JavaScript

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/JereStrath/Stego_Project001.git

2. Install the required dependencies
   pip install -r requirements.txt

3. Run the application:
   python api.py

4. Access the application in your web browser at `http://localhost:5000`.

## Usage
- Sign up for an account or log in with existing credentials.
- Upload a suspicious image using the provided form.
- Wait for the system to process the image and provide the stegomalware detection result.
- View the prediction result and take necessary actions based on the outcome.
- Log out when finished.

## File Structure
The project's file structure is organized as follows:

├── api.py                  # Main application file
├── models/                 # Directory to store trained models
├── static/                 # Static files (CSS, JavaScript, images)
├── templates/              # HTML templates
├── database.db             # SQLite database file
├── README.md               # Project documentation (you are here)
└── requirements.txt        # List of required dependencies

## Contributing 
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please submit a pull request.

## Authors 
Jeremiah Mwaura

## Acknowledgments
Special thanks to the open-source community for their valuable resources and inspiration. I want to extend my sincere appreciation to everyone who helped this senior project come to fruition and contributed to its success. First of all, I would want to express my sincere gratitude to my project manager, Mr. Bruce Totona, for their tremendous advice, support, and knowledge during the whole period of this project. The direction and caliber of this work were greatly influenced by their astute comments and helpful critique. I am also appreciative to Mr. Tiberius Tabulu, my project lecturer for providing the essential tools and supportive academic materials that assisted in the research and documentation process.I would want to express my sincere gratitude to my family and friends for their constant support, patience, and inspiration during the highs and lows of this endeavor. Their unwavering support and confidence in my skills acted as a motivating factor that propelled me in the direction of success. Last but not least, I would want to express my appreciation to all the researchers, writers, and academics whose study and writing served as the basis for this project, as well as the open-source community for making important tools and software available. 
