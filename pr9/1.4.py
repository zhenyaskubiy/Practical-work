import random
words = ['red', 'cat', 'orange', 'grape', 'cross', 'kiwi', 'peach', 'plum']

def generate_password(word_list):
    random_words = random.sample(word_list, 2)

    password = ''.join([word.capitalize() for word in random_words])

    while len(password) < 8 or len(password) > 10 or any(len(word) < 3 for word in random_words):
        random_words = random.sample(word_list, 2)
        password = ''.join([word.capitalize() for word in random_words])

    return password

generated_password = generate_password(words)
print("Згенерований пароль:", generated_password)

import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")