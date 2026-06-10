import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse



N = 3 # for simplicity and visualization
N_step = 10
eps = 1e-9

# Define the reservoir and input weights
W = np.random.randn(N, N) * 0.1
print(f"{W=}")


x0 = np.ones(N) #initial state
states = [x0]

def f(x_prev: np.ndarray): 
    return W @ x_prev
# some fixed function by the system

def step(states):
    x_next = f(states[-1])   #今まで計算した最後の
    states.append(x_next)


# Stepping

for _ in range(N_step):
    step(states)


# array -> nparray  
X = np.array(states)
print(f"{X=}")
print(f"{X.shape=}")
print(f"{states=}")

#1. Visualize Neurons
def plot1():
    fig, ax = plt.subplots()
    ax.plot(X)
    ax.set_xlabel("time step")
    ax.set_ylabel("state")
    ax.legend(["neuron 0", "neuron 1", "neuron 2"])
    plt.show()

#2. Visualize States(1)
def plot2():
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    T = X.shape[0]
    O = np.zeros(T)
    colors = plt.cm.viridis(np.linspace(0, 1, T))
    ax.quiver(O, O, O, X[:,0], X[:,1], X[:,2], colors = colors)
    ax.set_xlabel("x0")
    ax.set_xlabel("x1")
    ax.set_xlabel("x2")
    plt.show()

#3. Visualize States(1)
def plot3():
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    T = X.shape[0]
    colors = plt.cm.viridis(np.linspace(0, 1, T))

    L0 = np.abs(X).max()    *1.3
    Lend = np.abs(X[-1]).max()    *1.3

    n_frames = 200

    def update(frame):
        ax.clear()
        
        O = np.zeros(T)
        ax.quiver(O, O, O, X[:,0], X[:,1], X[:,2], colors=colors)
        r = frame / (n_frames - 1)
        L = L0 * (Lend / L0) ** r
        ax.set_xlim(-L,L);ax.set_ylim(-L,L);ax.set_zlim(-L,L);
        ax.set_box_aspect([1,1,1])
        ax.set_title(f"zoom L = {L:.10f}")
        
    ani = animation.FuncAnimation(fig, update, frames=n_frames, interval=30)
    plt.show()
    return ani

# For plot selection

PLOTS = {1: plot1,2: plot2,3: plot3}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("plots", nargs="*", type=int, default=[1, 2, 3],
                        help="type plotnumber to plot")
    args = parser.parse_args()

    for n in args.plots:
        PLOTS[n]()
