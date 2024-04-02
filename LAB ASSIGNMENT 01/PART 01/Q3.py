def string_to_integer(string):
    if not string:
        return 0
    
   
    return string_to_integer(string[:-1]) * 10 + int(string[-1])

input_string = input("Enter a string of digits: ")
result = string_to_integer(input_string)
print("The integer representation is:", "{:,}".format(result))
