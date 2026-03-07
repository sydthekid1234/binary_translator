def binary_to_text(binary_string):
    binary_string = binary_string.replace(" ", "")
    if len(binary_string) % 8 != 0:
        return "Error: Binary length must be a multiple of 8."
    text = ""
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        character = chr(int(byte, 2))
        text += character
    return text
binary_input = input("Enter binary code to translate: ")
message = binary_to_text(binary_input)
print("Translated text:", message)