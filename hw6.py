import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

sizes = [1000 * i for i in range(1, 30)]
iterations = 10
sigma = 1
gammas = [0.1, 0.5, 0.95]


def generate(count: int) -> np.ndarray:
    return np.random.normal(0, sigma, count)


def size1(values: np.ndarray, gamma: float) -> float:
    quantiles = st.chi2.ppf([(1 + gamma) / 2, (1 - gamma) / 2], len(values))
    return np.sum(values ** 2) * (1 / quantiles[1] - 1 / quantiles[0])


def size2(values: np.ndarray, gamma: float) -> float:
    quantiles = st.norm.ppf([(3 + gamma) / 4, (3 - gamma) / 4], 0, sigma)
    return len(values) * ((np.average(values)) ** 2) * (1 / (quantiles[1] ** 2) - 1 / (quantiles[0] ** 2))


def calc(generate, gamma, window_size, filename):
    ws = []
    for size in sizes:
        ws_sum = 0.0
        for _ in range(iterations):
            ws_sum += window_size(generate(size), gamma)
        ws.append(ws_sum / iterations)

    fig, ax = plt.subplots()
    ax.plot(sizes, ws)
    ax.set_ylabel("window size")
    ax.set_xlabel("dataset size")
    fig.savefig(filename)


for gamma in gammas:
    calc(generate, gamma, size1, f"{gamma}_1.png")
    calc(generate, gamma, size2, f"{gamma}_2.png")
