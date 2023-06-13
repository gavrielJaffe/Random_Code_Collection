#!/usr/bin/env python

# File name: list_flattening.py
# Purpose: Flatten a nested list and print the flattened list

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

# Function to flatten a nested list
def flatten(lists):
    results = []
    for lst in lists:
        for i in lst:
            results.append(i)
    return results


def main():
    # Print the flattened list
    print(flatten(n))
    # Alternatively, you can just call the function without printing the result:
    # flatten(n)

if __name__ == '__main__':
    main()
