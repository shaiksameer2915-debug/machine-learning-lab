import numpy as np
from sklearn.linear_model import LinearRegression

# Monthly sales data
months = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
sales = np.array([120, 135, 150, 160, 175, 190, 210, 220, 240, 260])

# Create and train model
model = LinearRegression()
model.fit(months, sales)

# Predict future sales
future_months = np.array([11, 12, 13, 14, 15]).reshape(-1, 1)
predicted_sales = model.predict(future_months)

print("Future Sales Prediction:")
for month, sale in zip(future_months, predicted_sales):
    print("Month", month[0], ":", round(sale, 2), "units")