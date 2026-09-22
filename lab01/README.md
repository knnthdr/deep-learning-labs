\## Laboratory 

Lab 1 — Building Your Deep Learning Workbench



\## Objective

In this laboratory, I set up and explored a basic deep learning environment using Google Colab, PyTorch, GitHub, and Hugging Face. I also tested a pretrained image classification model, examined its predictions, and explored an example where the model did not give the expected result.



\## Tools Used

\- Google Colab

\- GitHub



\## Model Used

The model tested was the \*\*Vision Transformer (ViT) model for Image Classification\*\*: `google/vit-base-patch16-224`.



\## Main Result



The model was able to classify different images and provide predictions with confidence scores. For example, it correctly identified an image as a sports car with a score of approximately 65.1%. The experiment also showed that the confidence score does not always mean that the prediction is correct.



\## Interesting Failure



One interesting failure occurred when I tested an image of an axial turbopump for an M-1 rocket engine. The model predicted that the image was a dumbbell with a score of aprox 47.9%. This is because of the large components on the left and right sides, which may have led the model to interpret it as a dumbbell. 

## Collab link: https://colab.research.google.com/drive/1DZdG_Sm8Z7Klxhac98ogiY3FgE9OR2Ws?usp=sharing
