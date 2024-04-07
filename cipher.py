alphabet = ''.join([chr(i) for i in range(ord('a'), ord('z') + 1)])

def cipher(char, key):
    index = alphabet.find(char)
    if char == ' ' or char not in alphabet:
        return char
    else:
        if (index + key) > len(alphabet):
            steps_left = key - len(alphabet[index + 1:])
            return alphabet[steps_left - 1]
        else:
            return alphabet[index + key]
    

def ceaser_cipher(phrase, key):
    new_phrase = phrase.lower()
    ciphered_text = ''
    for char in phrase:
        ciphered_char = cipher(char, key)
        ciphered_text += ciphered_char
    return ciphered_text.title()

print(ceaser_cipher('what a string!', 5))