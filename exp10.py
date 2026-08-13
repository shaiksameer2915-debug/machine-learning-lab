# Expectation-Maximization (EM) Algorithm
# Simple 1-D Gaussian Mixture Model

import math

# Data
data = [2, 3, 4, 5, 6, 15, 16, 17, 18, 19]

# Number of clusters
k = 2

# Initial values
mean1 = 4
mean2 = 16

variance1 = 2
variance2 = 2

weight1 = 0.5
weight2 = 0.5

# Gaussian probability function
def gaussian(x, mean, variance):
    return (1 / math.sqrt(2 * math.pi * variance)) * \
           math.exp(-((x - mean) ** 2) / (2 * variance))


# EM Algorithm
for iteration in range(10):

    # -------------------------
    # E-STEP
    # -------------------------
    responsibilities1 = []
    responsibilities2 = []

    for x in data:

        p1 = weight1 * gaussian(x, mean1, variance1)
        p2 = weight2 * gaussian(x, mean2, variance2)

        total = p1 + p2

        r1 = p1 / total
        r2 = p2 / total

        responsibilities1.append(r1)
        responsibilities2.append(r2)

    # -------------------------
    # M-STEP
    # -------------------------

    # Calculate total responsibilities
    N1 = sum(responsibilities1)
    N2 = sum(responsibilities2)

    # Update means
    mean1 = sum(
        responsibilities1[i] * data[i]
        for i in range(len(data))
    ) / N1

    mean2 = sum(
        responsibilities2[i] * data[i]
        for i in range(len(data))
    ) / N2

    # Update variances
    variance1 = sum(
        responsibilities1[i] * (data[i] - mean1) ** 2
        for i in range(len(data))
    ) / N1

    variance2 = sum(
        responsibilities2[i] * (data[i] - mean2) ** 2
        for i in range(len(data))
    ) / N2

    # Update weights
    weight1 = N1 / len(data)
    weight2 = N2 / len(data)

    print("Iteration", iteration + 1)
    print("Mean 1     :", round(mean1, 3))
    print("Mean 2     :", round(mean2, 3))
    print("Variance 1 :", round(variance1, 3))
    print("Variance 2 :", round(variance2, 3))
    print("Weight 1   :", round(weight1, 3))
    print("Weight 2   :", round(weight2, 3))
    print("----------------------------")


# -------------------------
# FINAL CLUSTER ASSIGNMENT
# -------------------------

print("\nFINAL CLUSTER ASSIGNMENT")
print("----------------------------")

for x in data:

    p1 = weight1 * gaussian(x, mean1, variance1)
    p2 = weight2 * gaussian(x, mean2, variance2)

    if p1 > p2:
        cluster = 1
    else:
        cluster = 2

    print("Data:", x, "-> Cluster:", cluster)