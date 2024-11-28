def shorten(word):  # 'word' is received here as an argument
    result = ""
    vowel = "aeiouAEIOU"
    # Omit vowel letters
    for l in word:
        if l not in vowel:
            result += l
    return result

def main():
    word = input("Enter a word: ")  # Taking input in main()
    print("Output:", shorten(word))  # Passing 'word' to shorten()

if __name__ == "__main__":
    main()
