#My-Codes-21 (Projects)
#this code checks the each combination of any num or alphapet
import itertools

def generate_combinations(input_string):
    # Generate all permutations of the input string
    permutations = [''.join(p) for p in itertools.permutations(input_string)]
    return permutations

# Example usage:
user_input = "My-Codes-21"  # write your num or alphabet here or any string of characters
combinations = generate_combinations(user_input)

print(f"Total combinations: {len(combinations)}")
for combo in combinations:
    print(combo)