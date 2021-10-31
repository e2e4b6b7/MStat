import numpy as np
import matplotlib.pyplot as plt

sizes = [1000 * i for i in range(1, 10)]
iterations = 30000
sigma = 1


def generate(count: int) -> np.ndarray:
    return np.random.normal(0, sigma, count)


def size1(values: np.ndarray) -> float:
    return np.sum(values ** 2)


def size2(values: np.ndarray) -> float:
    return len(values) * (np.average(values)) ** 2


def calc(generate, window_size, filename):
    ws = []
    for size in sizes:
        ws_sum = 0.0
        for _ in range(iterations):
            ws_sum += window_size(generate(size))
        ws.append(ws_sum / iterations)

    fig, ax = plt.subplots()
    ax.plot(sizes, ws)
    ax.set_ylabel("window size")
    ax.set_xlabel("dataset size")
    fig.savefig(filename)

calc(generate, size1, "1.png")
calc(generate, size2, "2.png")
