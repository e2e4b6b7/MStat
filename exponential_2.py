import numpy
import matplotlib.pyplot as plt
from math import factorial

size = 100000
k_values = [i for i in range(1, 10)] + [i for i in range(12, 30, 2)]
iterations = 100
theta = 1


def generate(count: int) -> numpy.ndarray:
    return numpy.random.exponential(theta, count)


def estimate(values: numpy.ndarray, k: int) -> float:
    return (numpy.average(values ** k_values[k_index]) / factorial(k)) ** (1 / k)


sd_sum = [0.0] * len(k_values)
for _ in range(iterations):
    generated = generate(size)
    for k_index in range(len(k_values)):
        sd_sum[k_index] += (theta - estimate(generated, k_values[k_index])) ** 2

sd = list(map(lambda x: x / iterations, sd_sum))

fig, ax = plt.subplots()
ax.plot(k_values, sd)
ax.set_ylabel("sd")
ax.set_xlabel("k")
fig.savefig("exponential_2.png")
