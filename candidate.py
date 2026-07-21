# Candidate Elimination Algorithm

# Training Data
concepts = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change']
]

# Target Values
target = ['Yes', 'Yes', 'No', 'Yes']

# Initialize Specific Hypothesis
specific = concepts[0].copy()

# Initialize General Hypothesis
general = [['?' for i in range(len(specific))]
           for j in range(len(specific))]

print("Initial Specific Hypothesis:")
print(specific)

print("\nInitial General Hypothesis:")
for row in general:
    print(row)

# Candidate Elimination Algorithm
for i in range(len(concepts)):

    if target[i] == "Yes":

        for j in range(len(specific)):

            if concepts[i][j] != specific[j]:
                specific[j] = '?'
                general[j][j] = '?'

    else:

        for j in range(len(specific)):

            if concepts[i][j] != specific[j]:
                general[j][j] = specific[j]
            else:
                general[j][j] = '?'

print("\nFinal Specific Hypothesis:")
print(specific)

print("\nFinal General Hypothesis:")
for row in general:
    print(row)