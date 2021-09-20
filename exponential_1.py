import numpy
import matplotlib.pyplot as plt
from math import factorial

sizes = [10000 * i for i in range(1, 15)]
k_values = [1, 2, 3, 4, 5]
iterations = 300
theta = 1


def generate(count: int) -> numpy.ndarray:
    return numpy.random.exponential(theta, count)


def estimate(values: numpy.ndarray, k: int) -> float:
    return (numpy.average(values ** k_values[k_index]) / factorial(k)) ** (1 / k)


sd = []

for size in sizes:
    sd_sum = [0.0] * len(k_values)
    for _ in range(iterations):
        generated = generate(size)
        for k_index in range(len(k_values)):
            sd_sum[k_index] += (theta - estimate(generated, k_values[k_index])) ** 2
    sd.append(list(map(lambda x: x / iterations, sd_sum)))

fig, ax = plt.subplots()
ax.plot(sizes, sd)
ax.legend(["k = {}".format(i) for i in k_values])
ax.set_ylabel("sd")
ax.set_xlabel("size")
fig.savefig("exponential_1.png")
