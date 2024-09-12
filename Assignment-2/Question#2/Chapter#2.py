def separate_and_convert(string):
    number_str = ""
    letter_str = ""
   
    # Separate numbers and uppercase letters
    for char in string:
        if char.isdigit():
            number_str += char
        elif char.isupper():
            letter_str += char
   
    # Convert numbers and letters to ASCII
    number_ascii = [ord(char) for char in number_str if char.isdigit() and int(char) % 2 == 0]
    letter_ascii = [ord(char) for char in letter_str]
   
    return number_str, letter_str, number_ascii, letter_ascii

# Example string
string = "56OawIWi984kst#Z352a07Vm415ss785gfs31Dio"

number_str, letter_str, number_ascii, letter_ascii = separate_and_convert(string)

print(f"Number String: {number_str}")
print(f"Letter String: {letter_str}")
print(f"Number ASCII Codes: {number_ascii}")
print(f"Letter ASCII Codes: {letter_ascii}")