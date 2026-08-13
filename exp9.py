# Compare Linear Regression and Polynomial Regression

# Training data
X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Y = [2, 5, 10, 17, 26, 37, 50, 65, 82, 101]

# -------------------------------
# LINEAR REGRESSION
# -------------------------------

x_mean = sum(X) / len(X)
y_mean = sum(Y) / len(Y)

numerator = 0
denominator = 0

for i in range(len(X)):
    numerator += (X[i] - x_mean) * (Y[i] - y_mean)
    denominator += (X[i] - x_mean) ** 2

m = numerator / denominator
c = y_mean - m * x_mean

print("LINEAR REGRESSION")
print("--------------------------")
print("Equation: Y =", round(m, 2), "X +", round(c, 2))


def linear_predict(x):
    return m * x + c


# -------------------------------
# POLYNOMIAL REGRESSION
# Y = aX^2 + bX + c
# -------------------------------

# For this example, use a quadratic model.
# Solve the three equations using normal equations.

n = len(X)

sum_x = sum(X)
sum_x2 = sum(x ** 2 for x in X)
sum_x3 = sum(x ** 3 for x in X)
sum_x4 = sum(x ** 4 for x in X)

sum_y = sum(Y)
sum_xy = sum(X[i] * Y[i] for i in range(n))
sum_x2y = sum((X[i] ** 2) * Y[i] for i in range(n))

# Matrix:
# [sum_x4  sum_x3  sum_x2] [a] = [sum_x2y]
# [sum_x3  sum_x2  sum_x ] [b] = [sum_xy]
# [sum_x2  sum_x   n     ] [c] = [sum_y]

# Gaussian elimination

A = [
    [sum_x4, sum_x3, sum_x2, sum_x2y],
    [sum_x3, sum_x2, sum_x,  sum_xy],
    [sum_x2, sum_x,  n,      sum_y]
]

# Convert matrix to upper triangular form
for i in range(3):
    pivot = A[i][i]

    for j in range(i + 1, 3):
        factor = A[j][i] / pivot

        for k in range(i, 4):
            A[j][k] = A[j][k] - factor * A[i][k]

# Back substitution
c_poly = A[2][3] / A[2][2]

b_poly = (A[1][3] - A[1][2] * c_poly) / A[1][1]

a_poly = (
    A[0][3]
    - A[0][2] * c_poly
    - A[0][1] * b_poly
) / A[0][0]

print("\nPOLYNOMIAL REGRESSION")
print("--------------------------")
print(
    "Equation: Y =",
    round(a_poly, 2), "X^2 +",
    round(b_poly, 2), "X +",
    round(c_poly, 2)
)


def polynomial_predict(x):
    return a_poly * x ** 2 + b_poly * x + c_poly


# -------------------------------
# COMPARISON
# -------------------------------

print("\nCOMPARISON")
print("--------------------------")

for x in [3, 5, 7, 9]:

    linear = linear_predict(x)
    polynomial = polynomial_predict(x)

    print("X =", x)
    print("Linear Prediction   :", round(linear, 2))
    print("Polynomial Prediction:", round(polynomial, 2))
    print("--------------------------")