import itertools

# Generate all combinations of 3 letters
combinations = [''.join(combination) for combination in itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=3)]

# Save the combinations to a text file
with open('combinations.txt', 'w') as file:
    for combination in combinations:
        file.write(combination + '\n')

print("Combinations saved to combinations.txt")
