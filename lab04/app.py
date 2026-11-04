import gradio as gr
import torch
import torch.nn as nn
from torchvision import transforms
from pathlib import Path


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

classes = [
    "crazing",
    "inclusion",
    "patches",
    "pitted_surface",
    "rolled_in_scale",
    "scratches"
]


class CNN(nn.Module):

    def __init__(self, num_classes=6):
        super(CNN, self).__init__()

        self.features = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(16, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(64 * 8 * 8, 128),
            nn.ReLU(),
            nn.Linear(128, num_classes)
        )

    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x


cnn_model = CNN(num_classes=len(classes))

weights_path = (
    Path(__file__).resolve().parent
    / "results"
    / "cnn_model.pth"
)

if not weights_path.exists():
    raise FileNotFoundError(
        f"Model weights not found at: {weights_path}"
    )

checkpoint = torch.load(
    weights_path,
    map_location=device,
    weights_only=True
)

if isinstance(checkpoint, dict) and "state_dict" in checkpoint:
    checkpoint = checkpoint["state_dict"]

elif isinstance(checkpoint, dict) and "model_state_dict" in checkpoint:
    checkpoint = checkpoint["model_state_dict"]

checkpoint = {
    key.replace("module.", ""): value
    for key, value in checkpoint.items()
}

cnn_model.load_state_dict(checkpoint)

cnn_model = cnn_model.to(device)
cnn_model.eval()


transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    transforms.Resize((64, 64)),
    transforms.ToTensor()
])


def predict_defect(image):

    if image is None:
        return {}

    image = transform(image)
    image = image.unsqueeze(0)
    image = image.to(device)

    with torch.no_grad():
        outputs = cnn_model(image)
        probabilities = torch.softmax(outputs, dim=1)[0]

    results = {}

    for class_name, probability in zip(
        classes,
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
        "Upload an image of a steel surface. "
        "The CNN will predict the defect category."
    )
)


if __name__ == "__main__":
    app.launch()
```
