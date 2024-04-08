import torch
from Cricket07Automation.model.model import AlexNet
import cv2
import numpy as np

class Prediction:
    def __init__(self) -> None:
        self.net = AlexNet()
        self.net.load_state_dict(torch.load("model/model_pth/model.pth", map_location=torch.device('cpu')))
        self.net.eval()

    def softmax(self, x):
        return np.exp(x) / np.sum(np.exp(x), axis=0)

    def predict(self, screenshot):
        x = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        x = cv2.resize(x, (227, 227))
        x = x[np.newaxis, :, :]

        tensor = torch.Tensor(x)

        outputs = self.net(tensor)
        probs = torch.nn.functional.softmax(outputs, dim=1)
        conf, predicted = torch.max(probs, 1)

        return predicted.item(), round((conf.item() * 100), 2)