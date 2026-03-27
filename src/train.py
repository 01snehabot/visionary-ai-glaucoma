import torch
from torchvision import models
from torch import nn

model = models.efficientnet_b0(pretrained=True)
model.classifier[1] = nn.Linear(1280, 2)

print("Model ready")
