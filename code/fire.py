import torch
import torch.nn as nn


class Net(nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden = nn.Linear(n_feature, n_hidden)
        self.output = nn.Linear(n_hidden, n_output)
        self.criterion = nn.MSELoss()
        self.optimizer = torch.optim.SGD(self.parameters(), lr=0.001)
        self.cuda()

    def forward(self, x):
        s = nn.Sigmoid()
        z1 = s(self.hidden(x))
        # z1 = self.hidden(x)
        z2 = self.output(z1)
        return z2

    def backward(self, z2, y):
        loss = self.criterion(z2, y)
        self.optimizer.zero_grad()
        return loss

    def trained(self, x, y):
        pre = self.forward(x)
        loss = self.backward(pre, y)
        loss.backward()
        self.optimizer.step()
        return pre, loss

def accuracy(preset, labelset):
    count = 0
    print(len(preset))
    for i in range(len(preset)):
        print(i)
        pre = preset[i]
        label = labelset[i]
        print(label)
        dis = ((pre[0] - label[0]) ** 2 + (pre[1] - label[1]) ** 2) ** (1 / 2)
        if dis < 0.5:
            count += 1
    return count/len(preset)

def accuracy2(pre, label):
    dis = ((pre[0] - label[0]) ** 2 + (pre[1] - label[1]) ** 2) ** (1 / 2)
    if dis < 0.5:
        return 1
    else:
        return 0

def accuracy3(pre, label):
    return ((pre[0] - label[0]) ** 2 + (pre[1] - label[1]) ** 2) ** (1 / 2)
