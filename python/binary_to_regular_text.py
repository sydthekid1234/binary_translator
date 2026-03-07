def binary_to_text(binary_string):
    binary_string = binary_string.replace(" ", "")
    text = ' '.join([chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8)])
    return text
binary_input = input("What binary code do you wan't to translate?")
message = binary_to_text(binary_input)
print(message)