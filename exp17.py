import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Data: [RAM(GB), Storage(GB), Battery(mAh), Camera(MP), Screen(inches)]
X = np.array([
    [2, 32, 3000, 12, 5.5],
    [3, 32, 3500, 13, 5.8],
    [4, 64, 4000, 16, 6.0],
    [4, 128, 4500, 20, 6.2],
    [6, 128, 5000, 48, 6.4],
    [8, 128, 5000, 64, 6.5],
    [8, 256, 5000, 64, 6.7],
    [12, 256, 6000, 108, 6.8],
    [12, 512, 6000, 108, 6.9],
    [6, 64, 4000, 24, 6.1]
])

# Price categories: 0=Low, 1=Medium, 2=High
y = np.array([0, 0, 1, 1, 1, 2, 2, 2, 2, 1])

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
print("Actual:   ", y_test)
print("Predicted:", y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Predict a new mobile
new_mobile = [[8, 256, 5000, 64, 6.6]]
prediction = model.predict(new_mobile)

prices = ["Low Price", "Medium Price", "High Price"]
print("Predicted Mobile Price:", prices[prediction[0]])