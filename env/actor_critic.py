import torch
import torch.nn as nn
import torchvision.models as models

# possible actions:
# move to (absolute position)
# move relative
# control peripherals
# read sensor
# wait
# send message
# take photo
# water plant
# plant plant
# suppress weed

class ActorCritic(nn.module):
    def __init__(self, hidden_size):
        super().__init__()
        self.hidden_size = hidden_size
        self.actions = {
            "water": -1,
            "sow_seed": 1,
            "measure_soil_moisture": 0,
            "take_photo": 0,
            "suppress_weed": 1
        }
        # table should be 2:1 ratio
        # -> input 256 x 512
        self.actor_bb = models.resnet34(pretrained=True)
        
    
        