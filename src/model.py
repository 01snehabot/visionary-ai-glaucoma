from torchvision import models
from torch import nn

def get_model():
    model = models.efficientnet_b0(pretrained=True)
    model.classifier[1] = nn.Linear(1280, 2)
    return model
