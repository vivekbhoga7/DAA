def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        
        reversed_substring = reverse_string(s[1:])
        
        return reversed_substring + s[0]

word = input("Enter a word of your choice : ")
print(reverse_string(word))