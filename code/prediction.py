import torch
import numpy as np
import fire

class Prediction:
    def __init__(self, feature):
        self.firemodel = fire.Net(9,11,2)
        self.feature = feature

    def getPrediction(self):
        psum = 0
        for i in range(25):
            self.firemodel.load_state_dict((torch.load('../mlp/20000_001_11_mesh01_Sigmoid_new3/mlp' + str(i) + '.params')))
            device = torch.device('cuda:0')
            tensor_f = torch.tensor(self.feature).to(torch.float32).to(device)

            pre = self.firemodel.forward(tensor_f)
            psum += pre
            print(pre)
        print(psum/25)
        return (psum/25)