# Chess detection project

## Purpose

This project is my attempt to learn and understand Computer Vision models. Everything is documented in the TrainingYOLO folder. "The Documentation of training YOLO.pdf" is the main file where I document the input and the graph results of each training session. The other files are notes on things I learned along the way or that are important for training the model.

## Info
- I am using the YOLO object detection model trained on [this](https://app.roboflow.com/juji-r0keo/chess-detection-hmuju-nyz9c/train) dataset and tuned with my custom dataset [here](https://app.roboflow.com/juji-r0keo/my-chess-pieces/annotate), which both are public on Roboflow.
- Collect_pictures.py is used to capture the images in my custom dataset with my camera. 
- detectChessPieces.py is used to test the trained model on images outside of its dataset, some of which are in the runs folder.
