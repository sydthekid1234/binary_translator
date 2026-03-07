def text_to_binary_ascii(text):
    binary_list = [format(ord(char), '08b') for char in text]
    return ' '.join(binary_list)

message = input("What would you like to turn into Binary?")
binary_output = text_to_binary_ascii(message)
print(binary_output)