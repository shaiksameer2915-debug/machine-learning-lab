import math

# Training Data
data = [
    ['Sunny', 'Hot', 'High', 'No'],
    ['Sunny', 'Hot', 'High', 'No'],
    ['Overcast', 'Hot', 'High', 'Yes'],
    ['Rain', 'Mild', 'High', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'No']
]

# Attribute Names
attributes = ['Outlook', 'Temperature', 'Humidity']

# Function to calculate Entropy
def entropy(dataset):

    yes = 0
    no = 0

    for row in dataset:
        if row[-1] == "Yes":
            yes += 1
        else:
            no += 1

    total = yes + no

    if yes == 0 or no == 0:
        return 0

    p_yes = yes / total
    p_no = no / total

    return -(p_yes * math.log2(p_yes) + p_no * math.log2(p_no))


# Find Best Attribute
best_attribute = ""
highest_gain = 0

total_entropy = entropy(data)

for col in range(3):

    values = []

    for row in data:
        if row[col] not in values:
            values.append(row[col])

    weighted_entropy = 0

    for value in values:

        subset = []

        for row in data:
            if row[col] == value:
                subset.append(row)

        weighted_entropy += (len(subset) / len(data)) * entropy(subset)

    gain = total_entropy - weighted_entropy

    print(attributes[col], "Information Gain =", round(gain, 3))

    if gain > highest_gain:
        highest_gain = gain
        best_attribute = attributes[col]

print("\nRoot Node is:", best_attribute)