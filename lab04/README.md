# Lab 4 – Steel Surface Defect Classification

## Problem

The engineering problem addressed in this lab is the automatic detection and classification of defects on steel surfaces using a Deep Neural Network (Deep NN) and a Convolutional Neural Network (CNN).

## Dataset

The dataset used is the NEU-CLS steel surface defect dataset. It contains six defect classes:

- Crazing: Fine cracks on the steel surface.
- Inclusion: Foreign materials or impurities within the steel.
- Patches: Irregular patch-like surface defects.
- Pitted Surface: Small pits or holes on the surface.
- Rolled-in Scale: Scale or oxide particles rolled into the steel.
- Scratches: Linear marks on the steel surface.

The dataset contains 1,800 grayscale images, with 300 images per class. The images are resized to 64 × 64 pixels before being used by the models.

## Deep Neural Network (Deep NN)

The fully connected Deep Neural Network uses flattened image pixels as its input.
- Flatten layer: Converts the 64 × 64 image into a vector of 4,096 values.
- Fully connected layer: 4,096 input features and 256 neurons, followed by ReLU.
- Fully connected layer: 256 neurons and 64 neurons, followed by ReLU.
- Output layer: 64 neurons and 6 output classes.

The model contains 1,065,670 trainable parameters.

## Convolutional Neural Network (CNN)
The CNN is designed to process image data by learning local visual features such as edges, textures, and patterns.

The CNN architecture consists of:
- Convolutional layer: 1 input channel and 16 filters.
- ReLU activation and Max Pooling.
- Convolutional layer: 16 input channels and 32 filters.
- ReLU activation and Max Pooling.
- Convolutional layer: 32 input channels and 64 filters.
- ReLU activation and Max Pooling.
- Flatten layer.
- Fully connected layer: 4,096 features and 128 neurons, followed by ReLU.
- Output layer: 128 neurons and 6 output classes.

The CNN contains 548,486 trainable parameters.


## Evaluation

### Test Accuracy

| Model 	| Test Accuracy |
|---		|---:		|
| Deep NN 	| 46.7% 	|
| Original CNN 	| 92.6% 	|
| Modified CNN 	| 96.8% 	|

The modified CNN achieved the highest test accuracy after changing the learning rate.

### Per-Class Performance – Original CNN

| Defect Class | Precision | Recall | F1-Score | Support |
|---|---:|---:|---:|---:|
| Crazing | 0.98 | 0.96 | 0.97 | 51 |
| Inclusion | 0.88 | 0.85 | 0.86 | 41 |
| Patches | 1.00 | 1.00 | 1.00 | 42 |
| Pitted Surface | 0.87 | 0.87 | 0.87 | 52 |
| Rolled-in Scale | 0.95 | 0.98 | 0.96 | 41 |
| Scratches | 0.89 | 0.91 | 0.90 | 43 |
| **Overall Accuracy** | | | **0.93** | **270** |

Patches achieved the highest recall, while inclusion achieved the lowest recall.

### Confusion Matrix – Original CNN

Rows represent the true classes, while columns represent the predicted classes.

| True Class | Crazing | Inclusion | Patches | Pitted Surface | Rolled-in Scale | Scratches |
|---|---:|---:|---:|---:|---:|---:|
| Crazing | 49 | 0 | 0 | 0 | 2 | 0 |
| Inclusion | 0 | 35 | 0 | 6 | 0 | 0 |
| Patches | 0 | 0 | 42 | 0 | 0 | 0 |
| Pitted Surface | 1 | 2 | 0 | 45 | 0 | 4 |
| Rolled-in Scale | 0 | 0 | 0 | 0 | 40 | 1 |
| Scratches | 0 | 3 | 0 | 1 | 0 | 39 |

### Major Failure Cases

The CNN's major classification errors include:

- Inclusion was incorrectly classified as pitted_surface 6 times.
- Pitted_surface was incorrectly classified as scratches 4 times.
- Scratches were incorrectly classified as inclusion 3 times.
- Crazing was incorrectly classified as rolled_in_scale 2 times.

These errors may be caused by similarities in grayscale intensity, contrast, and texture patterns between certain defect classes.

## Model Comparison

| Characteristic | Deep NN | CNN |
|---|---|---|
| Input Representation | Flattened pixels | 2D image |
| Uses Spatial Relationships | Limited | Yes |
| Local Feature Extraction | No | Yes |
| Weight Sharing | No | Yes |
| Test Accuracy | 46.7% | 92.6% |
| Parameter Count | 1,065,670 | 548,486 |

The CNN outperformed the fully connected Deep NN.

The CNN achieved 92.6% test accuracy compared to 46.7% for the Deep NN. It also used approximately half as many trainable parameters. This improvement can be explained by the CNN's ability to extract local visual features and recognize spatial relationships in images. Convolutional filters are shared across image locations, reducing the number of parameters and making the model more suitable for image classification.

## Application

A small Gradio application was developed to allow users to upload an image of a steel surface and receive a predicted defect class.

The application uses the trained CNN model weights stored in `results/cnn_model.pth`.


### How to Run the Application

1. Clone or download the GitHub repository.
2. Navigate to the `lab04` folder.
3. Install the required packages:
4. Run the application:
5. Upload a steel surface image.
6. The application returns the predicted defect class and the confidence scores for the six classes.

The application uses the saved model weights and does not need to retrain the CNN.

## Engineering Conclusion

The CNN is more reliable for classifying steel surface defects than the fully connected Deep NN. However, I would not use it without testing on real production images and human review. Incorrect predictions can lead to financial losses. The classifier should be used as a support tool for industrial inspection.
