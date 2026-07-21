# Training Data
data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

print("Training Data:")
for row in data:
    print(row)

# Initialize hypothesis
hypothesis = ['0'] * (len(data[0]) - 1)

print("\nInitial Hypothesis:")
print(hypothesis)

# Find-S Algorithm
for row in data:

    # Consider only positive examples
    if row[-1] == 'Yes':

        for i in range(len(hypothesis)):

            if hypothesis[i] == '0':
                hypothesis[i] = row[i]

            elif hypothesis[i] != row[i]:
                hypothesis[i] = '?'

print("\nFinal Hypothesis:")
print(hypothesis)