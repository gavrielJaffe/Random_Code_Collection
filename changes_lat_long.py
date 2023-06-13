import random
#  Takes a number y ,Changes the the digits from the end. 

def changes_in_lat_log(n):
    random_digits = ''.join([str(random.randint(0, 10)) for i in range(13)])
    n_str = str(n)  # Convert the float to a string
    n_modified = n_str[:-9] + random_digits
    return n_modified


def main():
    y = 41.73128821377282
    number = changes_in_lat_log(y)
    print('number', number)


if __name__ == '__main__':
    main()
