# Credit Score Classification
# Simple Machine Learning Classification Program

# Training data
# [Income, Credit History, Existing Loans]
# Credit History: 0 = Bad, 1 = Good
# Existing Loans: number of loans

data = [
    [20000, 0, 4, "Poor"],
    [25000, 0, 3, "Poor"],
    [30000, 0, 2, "Poor"],
    [35000, 1, 3, "Average"],
    [40000, 1, 2, "Average"],
    [45000, 1, 1, "Good"],
    [50000, 1, 1, "Good"],
    [60000, 1, 0, "Good"],
    [70000, 1, 0, "Good"]
]

# Display training data
print("CREDIT SCORE CLASSIFICATION")
print("-----------------------------")

for record in data:
    print(
        "Income:", record[0],
        "Credit History:", record[1],
        "Loans:", record[2],
        "Score:", record[3]
    )

# Function to classify credit score
def classify(income, history, loans):

    if income < 30000 and history == 0:
        return "Poor"

    elif income < 45000 or loans >= 3:
        return "Average"

    else:
        return "Good"


# Test data
print("\nNEW CUSTOMER PREDICTIONS")
print("-----------------------------")

customers = [
    [22000, 0, 4],
    [38000, 1, 2],
    [55000, 1, 1],
    [65000, 1, 0]
]

for customer in customers:

    income = customer[0]
    history = customer[1]
    loans = customer[2]

    result = classify(income, history, loans)

    print("Income:", income)
    print("Credit History:", history)
    print("Existing Loans:", loans)
    print("Credit Score Classification:", result)
    print("-----------------------------")