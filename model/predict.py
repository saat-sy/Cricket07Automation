import torch
from Cricket07Automation.model.model import AlexNet
import cv2
import numpy as np

class Prediction:
    def __init__(self) -> None:
        self.net = AlexNet()
        self.net.load_state_dict(torch.load("model/model_pth/model.pth", map_location=torch.device('cpu')))
        self.net.eval()

    def predict(self, screenshot):
        x = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        x = cv2.resize(x, (227, 227))
        x = x[np.newaxis, :, :]

        tensor = torch.Tensor(x)

        outputs = self.net(tensor)
        _, predicted = torch.max(outputs, 1)

        return predicted.item()