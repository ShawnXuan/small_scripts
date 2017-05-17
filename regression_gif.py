import torch
from torch.autograd import Variable
import torch.nn.functional as F

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)  # x data (tensor), shape=(100, 1)
y = x.pow(2) + 0.2*torch.rand(x.size())                 # noisy y data (tensor), shape=(100, 1)

x, y = torch.autograd.Variable(x), Variable(y)

# plot
fig, ax = plt.subplots()
fig.set_tight_layout(True)

ax.scatter(x.data.numpy(), y.data.numpy())


class Net(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, n_hidden)   # hidden layer
        self.predict = torch.nn.Linear(n_hidden, n_output)   # output layer

    def forward(self, x):
        x = F.relu(self.hidden(x))      # activation function for hidden layer
        x = self.predict(x)             # linear output
        return x

net = Net(n_feature=1, n_hidden=10, n_output=1)     # define the network
print(net)  # net architecture

optimizer = torch.optim.SGD(net.parameters(), lr=0.5)
loss_func = torch.nn.MSELoss()  # this is for regression mean squared loss

iteration = 100
steplength = 5
pred = {}
# plot the initial line.
pred[0] = net(x)
line, = ax.plot(x.data.numpy(), pred[0].data.numpy(), 'r-', lw=5)

def update(i):
    label = 'timestep {0}'.format(i)
    print(label)
    # Update the line and the axes (with a new xlabel). Return a tuple of
    # "artists" that have to be redrawn for this frame.
    line.set_ydata(pred[i].data.numpy())
    ax.set_xlabel(label)
    return line, ax

if __name__ == '__main__':
    
    for t in range(iteration):
        prediction = net(x)     # input x and predict based on x
    
        loss = loss_func(prediction, y)     # must be (1. nn output, 2. target)
    
        optimizer.zero_grad()   # clear gradients for next train
        loss.backward()         # backpropagation, compute gradients
        optimizer.step()        # apply gradients
        if t % steplength == 0:
            pred[t/steplength] = prediction
            # FuncAnimation will call the 'update' function for each frame; here
            # animating over 20 frames, with an interval of 200ms between frames.
    anim = FuncAnimation(fig, update, frames=np.arange(0, iteration/steplength), interval=200)
    anim.save('regression.gif', dpi=80, writer='imagemagick')

