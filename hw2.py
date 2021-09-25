import numpy as np
from numpy import ndarray
import matplotlib.pyplot as plt
import heapq
from utils import transpose


def simulate1(n: int, alpha: float) -> ndarray:
    return np.sort(np.random.exponential(alpha, n))


def simulate2(n: int, alpha: float) -> ndarray:
    initials = np.random.exponential(alpha, n)
    secondaries = np.random.exponential(alpha, n)
    heap = list(initials)
    heapq.heapify(heap)
    waiting_time = []
    for i in range(n):
        outer = heapq.heappop(heap)
        waiting_time.append(outer)
        heapq.heappush(heap, outer + secondaries[i])
    return np.array(waiting_time)


experiments = [simulate1, simulate2]
ns = [100, 10000]
alphas = [1 / 2, 1, 2]
repetitions = 300

for experiment in experiments:
    for n in ns:
        valuess = []
        for alpha in alphas:
            values = np.zeros(n)
            for _ in range(repetitions):
                values += experiment(n, alpha)
            values /= repetitions
            valuess.append(values)

        fig, ax = plt.subplots()
        ax.plot([i for i in range(n)], transpose(valuess))
        ax.legend(["alpha = {}".format(alpha) for alpha in alphas])
        ax.set_ylabel("time")
        ax.set_xlabel("k")
        fig.savefig("{}_{}.png".format(experiment.__name__, n))
