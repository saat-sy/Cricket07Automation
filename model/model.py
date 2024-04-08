import torch
import torch.nn as nn

class AlexNet(nn.Module):
    def __init__(self, in_channels=1, num_classes=5):
        super(AlexNet, self).__init__()
        self.net = nn.Sequential(
            nn.Conv2d(in_channels=in_channels, out_channels=96, kernel_size=11, stride=4),  # (8 x 96 x 55 x 55)
            nn.ReLU(),
            nn.LocalResponseNorm(size=5, alpha=0.0001, beta=0.75, k=2),
            nn.MaxPool2d(kernel_size=3, stride=2),  # (8 x 96 x 27 x 27)
            nn.Conv2d(96, 256, 5, padding=2),  # (8 x 256 x 27 x 27)
            nn.ReLU(),
            nn.LocalResponseNorm(size=5, alpha=0.0001, beta=0.75, k=2),
            nn.MaxPool2d(kernel_size=3, stride=2),  # (8 x 256 x 13 x 13)
            nn.Conv2d(256, 384, 3, padding=1),  # (8 x 384 x 13 x 13)
            nn.ReLU(),
            nn.Conv2d(384, 384, 3, padding=1),  # (8 x 384 x 13 x 13)
            nn.ReLU(),
            nn.Conv2d(384, 256, 3, padding=1),  # (8 x 256 x 13 x 13)
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=3, stride=2),  # (8 x 256 x 6 x 6)
        )
        self.linear = nn.Sequential(
            nn.Dropout(p=0.5, inplace=False),
            nn.Linear(in_features=(256 * 6 * 6), out_features=4096),
            nn.ReLU(),
            nn.Dropout(p=0.5, inplace=False),
            nn.Linear(in_features=4096, out_features=4096),
            nn.ReLU(),
            nn.Linear(in_features=4096, out_features=num_classes),
        )

    def forward(self, x):
        x = self.net(x)
        x = x.view(-1, 256 * 6 * 6)
        return self.linear(x)