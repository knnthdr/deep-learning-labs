
import gradio as gr
import torch

from PIL import Image

def predict_defect(image):
    image = transform(image)
    image = image.unsqueeze(0)
    image = image.to(device)

    cnn_model.eval()

    with torch.no_grad():
        outputs = cnn_model(image)
        probabilities = torch.softmax(outputs, dim=1)[0]

    results = {}

    for class_name, probability in zip(
        dataset.classes,
        probabilities.cpu().numpy()
    ):
        results[class_name] = float(probability)

    return results


app = gr.Interface(
    fn=predict_defect,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=6),
    title="Steel Surface Defect Classifier",
    description=(
        "Upload an image of a steel surface and "
        "the CNN will predict the defect type."
    )
)

app.launch()
