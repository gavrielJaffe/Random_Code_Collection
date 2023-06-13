score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def scrabble_score(word):
    lowercase_word = word.lower()  # Convert word to lowercase
    total_score = 0
    for letter in lowercase_word:
        total_score += score[letter]  # Add the score of each letter to the total score
    return total_score

def main():
    some_string = 'piZZa'  # Example word
    print(scrabble_score(some_string))  # Print the scrabble score of the word

if __name__ == "__main__":
    main()
