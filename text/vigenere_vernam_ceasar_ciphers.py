key = "jeffmaxim"
message = "Is the best person ever!"
import pudb


def extend_key(key, message):
    message_length = len(message)
    key_length = len(key)
    if key_length < message_length:
        multiplier = (message_length / key_length) + 1
        longer_key = "".join([key] * multiplier)
        return longer_key
    return key

def ascii_converter(char):
    return ord(char) - 97 if char.islower() else ord(char) - 65


def vigenerize(char, index, key):
    if char.isalpha() is not True:
        return char

    # get ascii value of key_char
    key_char = key[index]
    offset = ascii_converter(key_char) 

    #get ascii value of chr
    char_ascii = ascii_converter(char) 
    # get rotated number
    new_char = (char_ascii + offset) % 26 
    new_char = 97 + new_char if char.islower() else 65 + new_char 
    return chr(new_char)


def vigenere_encypher(key, message):
    key = extend_key(key, message)
    # get each char in message
    message_list = list(message)
    # encypher each char
    encyphered_list = []
    i = 0
    for a in message:
        if a.isalpha() is not True:
            encyphered_list.append(a)
        else:
            encyphered_list.append(vigenerize(a, i, key))
            i += 1
    return encyphered_list

print vigenere_encypher(key, message)


