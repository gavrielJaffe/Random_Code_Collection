# Code to print each character in a string using different printing methods

def main():
    # num = input("Enter input: ")    # Commented out input prompt
    word = "eggs!"    # String to iterate through
    for w in word:
        # ways to print in python strings.
        # print("%s"%w)     # Example of older-style string formatting
        print(f"{w}")     # Example of f-string formatting

if __name__ == '__main__':
    main()
