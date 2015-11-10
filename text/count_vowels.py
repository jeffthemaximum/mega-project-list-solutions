# Count Vowels - Enter a string and the program counts the number of vowels in the text. 
# For added complexity have it report a sum of each vowel found.

sentence = "This is a sentence in which my program will count the vowels."
sentence2 = "378937"
sentence3 = "yhmn"

vowels = ["a", "e", "i", "o", "u"]


def count_vowels(string):
    count = 0
    for c in string:
        if c in vowels:
            count += 1
    return count

print count_vowels(sentence)
# returns 0
print count_vowels(sentence2)
# returns 0
print count_vowels(sentence3)
