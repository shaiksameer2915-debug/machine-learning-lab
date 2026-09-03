import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Data: [Income, Loan Amount, Credit Score, Age]
X = np.array([
    [30000, 10000, 650, 25],
    [45000, 15000, 700, 30],
    [60000, 20000, 750, 35],
    [25000, 12000, 600, 24],
    [80000, 30000, 800, 40],
    [35000, 18000, 620, 28],
    [90000, 25000, 780, 45],
    [50000, 10000, 720, 32],
    [20000, 15000, 580, 22],
    [70000, 20000, 760, 38]
])

# 1 = Loan Approved, 0 = Loan Rejected
y = np.array([1, 1, 1, 0, 1, 0, 1, 1, 0, 1])

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Naive Bayes model
model = GaussianNB()

# Train model
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

print("Actual:   ", y_test)
print("Predicted:", y_pred)

# Calculate accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Predict a new loan application
new_customer = [[55000, 15000, 730, 33]]
prediction = model.predict(new_customer)

if prediction[0] == 1:
    print("Loan Status: Approved")
else:
    print("Loan Status: Rejected")