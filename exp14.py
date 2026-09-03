import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Data: [Area in sq.ft, Bedrooms, Age of house]
X = np.array([
    [1000, 2, 10],
    [1200, 2, 8],
    [1500, 3, 5],
    [1800, 3, 3],
    [2000, 4, 2],
    [900, 2, 15],
    [1600, 3, 7],
    [2200, 4, 1],
    [1300, 3, 10],
    [2500, 4, 2]
])

# House prices in Lakhs
y = np.array([35, 42, 55, 70, 85, 30, 60, 95, 48, 110])

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Linear Regression model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

print("Actual Prices:   ", y_test)
print("Predicted Prices:", np.round(y_pred, 2))

# Evaluate model
print("R2 Score:", round(r2_score(y_test, y_pred), 2))

# Predict price of a new house
new_house = [[1700, 3, 5]]
price = model.predict(new_house)

print("Predicted House Price: ₹", round(price[0], 2), "Lakhs")