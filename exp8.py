# Linear Regression - Simple Python Program

# Training data
# X = Hours studied
# Y = Marks obtained

X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Y = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65]

# Calculate mean
x_mean = sum(X) / len(X)
y_mean = sum(Y) / len(Y)

# Calculate slope (m)
numerator = 0
denominator = 0

for i in range(len(X)):
    numerator += (X[i] - x_mean) * (Y[i] - y_mean)
    denominator += (X[i] - x_mean) ** 2

m = numerator / denominator

# Calculate intercept (c)
c = y_mean - m * x_mean

# Regression equation
print("Linear Regression Equation:")
print("Y =", round(m, 2), "X +", round(c, 2))

# Prediction function
def predict(x):
    return m * x + c

# Test values
test_values = [3, 5, 7, 9]

print("\nPredictions:")
print("----------------------")

for x in test_values:
    y = predict(x)
    print("Hours Studied:", x)
    print("Predicted Marks:", round(y, 2))
    print("----------------------")