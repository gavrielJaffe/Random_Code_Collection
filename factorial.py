import time
from unittest import result 

def factorial(x):
    t1 = time.time()
    times_to_iterate = int(x)
    sum = 1 
    for i in range(times_to_iterate):
        if i != 0 :
            sum += sum * i
    sum_time = time.time()-t1
    return sum , sum_time 


def factorial1(x):
    t1 = time.time()
    total = 1
    while x>0:
        print(x)
        total *= x
        x-=1
    sum_time = time.time()-t1
    return total , sum_time

def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        print(word)
        l -= 1
    return word
  
def anti_vowel(text):
    result = ' '
    valuse = 'ieaouIEAOU'
    for char in text:
        if char not in valuse:
            result += char 
    # print(result)
    return result


def main():
    txt = "i*biiioooeeaa**bb"
    print(anti_vowel(txt))



if __name__ == "__main__":
    main()