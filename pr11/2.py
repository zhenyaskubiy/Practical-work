import re

with open('wordlist.txt', 'r') as file:
    wordlist =set(word.strip().lower() for word in file.readlines())
def check(filename):
    misspelled_words = set()
    with open(filename, 'r') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
        for word in words:
            if word not in wordlist:
                misspelled_words.add(word)
    return misspelled_words

misspelled = check('text.txt')

if misspelled:
    print("Некоректно написані слова:")
    for word in misspelled:
        print(word)
else:
    print("У тексті немає некоректно написаних слів.")
