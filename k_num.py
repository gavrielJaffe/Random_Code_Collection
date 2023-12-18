import itertools


def challenge_string(text):
    k = text[0] # comes with each text in the start , and is the the amount of letters that we are counting in the text
    substring = (text[1::])
    print(substring)
    char_substr = set (substring)
    find_comination(char_substr,k)

    return None # Output: ebebebc


def find_comination(my_set,k):# Give all of the combination from this my_set in len(k).
    print('my_set', my_set)
    letters = ''
    
    for i in my_set:
        # if len(letters) < int(k):
        letters = letters + i 
    print('letters', letters)

    my_set = {'b', 'c', 'e', 'a'}

    permutations = list(itertools.permutations(my_set, int(k)))
    print(f"Permutations of length {int(k)}: {permutations}")
    print(f"Per len: {len(permutations)}")



def main():
    ans = challenge_string("3abbaebebebc")
    return ans
if __name__=="__main__":
    main()