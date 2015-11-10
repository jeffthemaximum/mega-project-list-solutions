import re
import pudb

banana = "Banana"
sentence = "This is a sentence."
vowels = ["a", "e", "i", "o", "u"]


def check_if_first_letter_is_vowel(string):
    first_letter = string[0]
    return True if first_letter in vowels else False


def split_sentence_into_array_of_strings(sentence):
    # splits sentence into words and puncuation
    return re.findall(r"[\w']+|[.,!?;]", sentence)


def get_first_consonants(word):
    consonants = []
    char_array = list(word)
    for c in word:
        if c in vowels:
            consonants = "".join(consonants)
            return consonants
        else:
            consonants.append(c)
    consonants = "".join(consonants)
    return consonants


def put_first_consonants_at_end(word):
    word = list(word)
    first_consonants = get_first_consonants(word)
    word.append(first_consonants)
    del word[0:len(first_consonants)]
    return ("").join(word)


def add_ay_to_word(word):
    word_with_ay = word + "ay"
    return word_with_ay


def add_yay_to_word(word):
    word_with_yay = word + "yay"
    return word_with_yay


def pig_latinitize_consonant_word(word):
    first_letter_at_end = put_first_consonants_at_end(word)
    pig_latin_word = add_ay_to_word(first_letter_at_end)
    return pig_latin_word


def pig_latinitize_vowel_word(word):
    pig_latin_word = add_yay_to_word(word)
    return pig_latin_word


def pig_latinitize_string(string):
    # for single words
    if (" ") not in string:
        # if first letter of word is vowel
        if check_if_first_letter_is_vowel(string):
            return pig_latinitize_vowel_word(string)
        # if first letter of word is consonant
        else:
            return pig_latinitize_consonant_word(string)
    else:
        pig_latin_array = []
        split_sentence = split_sentence_into_array_of_strings(string)
        for word in split_sentence:
            # check if word isn't letters (nums, puncutation, etc.)
            if word.isalpha() is not True:
                pig_latin_array.append(word)
            elif check_if_first_letter_is_vowel(word):
                new_word = pig_latinitize_vowel_word(word)
                pig_latin_array.append(" " + new_word)
            else:
                new_word = pig_latinitize_consonant_word(word)
                pig_latin_array.append(" " + new_word)
    return "".join(pig_latin_array).rstrip().lstrip()

print pig_latinitize_string(sentence)
print pig_latinitize_string(banana)
