# MNIST Model Architecture

This GitHub repository contains the code and documentation for a Convolutional Neural Network (CNN) model designed to classify images from the MNIST dataset. The repository also includes an image, `logs.png`, which is located in the `training` folder, illustrating the training logs and performance metrics.

## Table of Contents
- [Introduction](#introduction)
- [Usage](#usage)
- [Training](#training)
- [Results](#results)
- [License](#license)

## Introduction

The MNIST dataset is a widely used dataset in the field of machine learning and computer vision. It consists of 28x28 pixel grayscale images of handwritten digits (0-9) and their corresponding labels. The goal of this project is to build a CNN model to accurately classify these digits.

## Usage

To use this repository, follow these steps:

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/bipin-saha/MNIST_HWDR_WebApp.git
   ```

2. Navigate to the project directory:

   ```
   cd mnist-model-architecture
   ```

3. You can now explore the code and model architecture in the repository.

## Training

To train the CNN model, you can use the provided Python scripts. You may need to install the necessary Python libraries and dependencies, which can be found in the `requirements.txt` file. To install them, use the following command:

```
pip install -r requirements.txt
```

Once the dependencies are installed, you can initiate training using the `train.py` script:

```
python train.py
```

This script will start training the model on the MNIST dataset. You can customize hyperparameters and network architecture in the script to suit your requirements.

## Results

During training, various performance metrics and logs are recorded. Below is an example image (`logs.png`) showing the training logs and performance metrics:

![Training Logs](/training/logs.png)

This image provides valuable insights into the training process, including loss and accuracy over time.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. Feel free to use, modify, and distribute this code for your own projects.
