import torch
from torch import nn


class ConvBlock(nn.Module):
    def __init__(self, in_channels, out_channels, stride=1):
        super().__init__()
        self.block = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, 3, stride, 1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.SiLU(),
        )

    def forward(self, x):
        return self.block(x)


class TinyDetector(nn.Module):
    def __init__(self, width=32, neck_depth=2, num_classes=5):
        super().__init__()
        self.backbone = nn.Sequential(ConvBlock(3, width, 2), ConvBlock(width, width * 2, 2))
        self.neck = nn.Sequential(*[ConvBlock(width * 2, width * 2) for _ in range(neck_depth)])
        self.head = nn.Conv2d(width * 2, 5 + num_classes, 1)

    def forward(self, images):
        return self.head(self.neck(self.backbone(images)))

