def is_palindrome(s):
    if len(s) <= 1:
        print("the word is  palindrome")
    elif s[0] != s[-1]:
        print("the word is not palindrome")

    else:
        return is_palindrome(s[1:-1])


word = input("Enter a word of your choice : ")
print(is_palindrome(word))