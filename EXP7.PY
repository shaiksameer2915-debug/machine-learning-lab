# Logistic Regression - Simple Python Program

import math

# Training data
# [Hours studied, Attendance]
X = [
    [1, 50],
    [2, 55],
    [3, 60],
    [4, 65],
    [5, 70],
    [6, 75],
    [7, 80],
    [8, 85],
    [9, 90],
    [10, 95]
]

# 0 = Fail, 1 = Pass
Y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

# Initial weights and bias
w1 = 0
w2 = 0
b = 0

learning_rate = 0.01
epochs = 1000

# Sigmoid function
def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# Training
for epoch in range(epochs):

    dw1 = 0
    dw2 = 0
    db = 0

    for i in range(len(X)):
        z = w1 * X[i][0] + w2 * X[i][1] + b
        prediction = sigmoid(z)

        error = prediction - Y[i]

        dw1 += error * X[i][0]
        dw2 += error * X[i][1]
        db += error

    # Update weights
    w1 = w1 - learning_rate * dw1
    w2 = w2 - learning_rate * dw2
    b = b - learning_rate * db


# Prediction function
def predict(hours, attendance):
    z = w1 * hours + w2 * attendance + b
    probability = sigmoid(z)

    if probability >= 0.5:
        result = "PASS"
    else:
        result = "FAIL"

    return probability, result


# Test students
students = [
    [3, 60],
    [6, 75],
    [8, 85],
    [10, 95]
]

print("LOGISTIC REGRESSION RESULTS")
print("--------------------------------")

for student in students:
    probability, result = predict(student[0], student[1])

    print("Hours Studied :", student[0])
    print("Attendance    :", student[1], "%")
    print("Probability   :", round(probability, 2))
    print("Prediction    :", result)
    print("--------------------------------")