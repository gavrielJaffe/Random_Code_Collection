

def revers_text(text):
    return text[::-1]

def revers_text_using_str(text):
    new_text = ""
    for char in text:
        new_text = new_text + char
    return new_text

def main():
    print(revers_text_using_str("olleh"))

if __name__ == '__main__':
    main()
