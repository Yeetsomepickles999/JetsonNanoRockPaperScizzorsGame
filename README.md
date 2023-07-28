# Rock Paper Scissors Game using Modified ImageNet and ResNet-18

![Rock Paper Scissors](https://www.nvidia.com/content/dam/en-zz/Solutions/intelligent-machines/embedded-systems/jetson-nano/nvidia-jetson-nano-og.jpg)

Welcome to the Rock Paper Scissors Game GitHub project! This project utilizes a modified version of the ImageNet dataset and the ResNet-18 model to create a fun and interactive game of Rock Paper Scissors using your camera. The game allows you to play against the computer, which uses the power of deep learning to predict your hand gesture in real-time.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Training Your Own Model](#training-your-own-model)
- [How it Works](#how-it-works)
- [Best Results with Green Wallpaper](#best-results-with-green-wallpaper)
- [Contributing](#contributing)
- [GitHub Repository](#github-repository)
- [YouTube Demo](#youtube-demo)

## Introduction

The Rock Paper Scissors Game is a computer vision-based project that demonstrates the capabilities of deep learning models for hand gesture recognition. The ImageNet dataset has been modified and augmented with images of Rock, Paper, and Scissors hand gestures. These modified images were used to train the ResNet-18 model to recognize the specific gestures required for the game.

## Requirements

To run this project, you will need the following dependencies:

- Python 3.x
- PyTorch
- OpenCV
- NumPy

You will also need to install the `jetson_inference` and `jetson_utils` libraries for the functionality of `my-recognition.py`. These libraries provide the necessary tools for running the deep learning model on NVIDIA Jetson platforms.

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/Yeetsomepickles999/JetsonNanoRockPaperScizzorsGame.git
```

2. Navigate to the project directory:

```bash
cd JetsonNanoRockPaperScizzorsGame
```

3. Replace `imagenet.py` with the provided version:

Replace the `imagenet.py` file in the `jetson-inference/python/examples` directory with the provided version from this repository. This modified `imagenet.py` file contains the necessary modifications to fit the custom images for Rock, Paper, and Scissors gestures.

4. Upload your trained model:

Place your trained ResNet-18 model in ONNX format (`model.onnx`) in the `jetson-inference/python/examples` directory. As there is no given model in this repository, you will need to train your own model based on your dataset. See the [Training Your Own Model](#training-your-own-model) section for instructions on training your model.

5. Install Jetson Inference and Jetson Utils libraries:

For NVIDIA Jetson platforms, these libraries are essential for running the deep learning model and utilizing camera functionalities. Follow the steps below to install them:

- **Jetson Inference**:

```bash
git clone https://github.com/dusty-nv/jetson-inference
cd jetson-inference
git submodule update --init
mkdir build
cd build
cmake ../
make
sudo make install
sudo ldconfig
```

- **Jetson Utils**:

```bash
git clone https://github.com/dusty-nv/jetson-utils
cd jetson-utils
mkdir build
cd build
cmake ../
make
sudo make install
sudo ldconfig
```

Please note that these libraries are specifically designed for NVIDIA Jetson platforms. If you are using a different system, you may need to adapt the installation instructions accordingly.

## Usage

1. Ensure your camera is connected and accessible by the system.

2. Navigate to the `jetson-inference/python/examples` directory:

```bash
cd jetson-inference/python/examples
```

3. Run the Rock Paper Scissors game:

```bash
python my-recognition.py
```

4. Follow the on-screen instructions to play the game. When prompted, show your hand gesture (rock, paper, or scissors) in front of the camera, and the computer will make its choice simultaneously. The game will then determine the winner and display the result.

## Training Your Own Model

If you wish to train your own model based on your dataset, follow these steps:

1. Switch to the "master" branch: To access the necessary files and scripts for training the model, switch to the "master" branch of this repository.

```bash
git checkout master
```

2. Prepare your dataset: Create a dataset with images of Rock, Paper, and Scissors hand gestures. Organize the images into separate folders, with each folder representing a different gesture.

3. Modify `imagenet.py`: Use the provided `imagenet.py` script in the `jetson-inference/python/examples` directory as a starting point. Modify it to load your custom dataset and fine-tune the ResNet-18 model.

4. Train the model: Use the modified `imagenet.py` script to train the model on your dataset. Fine-tune the ResNet-18 model with the images of Rock, Paper, and Scissors.

5. Export the model: After training, export the trained model in ONNX format (`model.onnx`).

6. Upload the model: Place the `model.onnx` file in the `jetson-inference/python/examples` directory as mentioned in the installation instructions.

## How it Works

The Rock Paper Scissors Game uses the modified ImageNet dataset, which includes images of Rock, Paper, and Scissors hand gestures. These images were used to fine-tune the ResNet-18 deep learning model specifically for the Rock Paper Scissors game.

During the game, the camera captures real-time video input. The program processes each frame, detects the hand gesture using the fine-tuned ResNet-18 model, and predicts the corresponding gesture.

The game logic then determines the winner based on the traditional Rock Paper Scissors rules.

## Best Results with Green Wallpaper

For the best results and accurate hand gesture recognition, we recommend using a green wallpaper or green background behind your hand gesture during gameplay. The green color provides a high contrast against the skin tone, making it easier for the computer vision model to detect and recognize hand gestures effectively.

## Contributing

Contributions to this project are more than welcome! If you have ideas for improvements or new features, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or improvement.

3. Make your changes and commit them with descriptive commit messages.

4. Push your changes to your forked repository.

5. Open a pull request to this repository, explaining your changes and the benefits they provide.

## GitHub Repository

Find the project on GitHub: [https://github.com/Yeetsomepickles999/JetsonNanoRockPaperScizzorsGame](https://github.com/Yeetsomepickles999/JetsonNanoRockPaperScizzorsGame)

## YouTube Demo

Watch a description of the game on Youtube: [https://youtu.be/emMJ9Opf86Q](https://youtu.be/emMJ9Opf86Q)
Watch the game in action on YouTube: [https://youtu.be/_7Gh36yrx5g](https://youtu.be/_7Gh36yrx5g)
