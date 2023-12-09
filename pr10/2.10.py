import random

# Символи та їх вартість
symbols = {
    u"\U0001F352": "Cherry",
    u"\U0001F514": "Bell",
    u"\U0001F34B": "Lemon",
    u"\U0001F34A": "Orange",
    u"\u2606": "Star",
    u"\U0001F480": "Skull"
}
def one_armed_bandit():
    credit = 100
    bet = 5

    while credit >= bet:
        input("Натисніть Enter, щоб запустити бандита...")

        credit -= bet
        symbols_list = [random.choice(list(symbols.keys())) for _ in range(3)]

        print("Результат:")
        print(" ".join(symbols_list))

        if len(set(symbols_list)) == 1:
            if symbols[symbols_list[0]] == "Bell":
                print("Ви виграли 100 грн!")
                credit += 100
            else:
                print("Ви виграли 25 грн!")
                credit += 25
        elif len(set(symbols_list)) == 2:
            if symbols_list.count(u"\U0001F480") == 2:
                print("Ви втратили 5 грн!")
                credit -= 5
            else:
                print("Ви виграли 10 грн!")
                credit += 10
        else:
            print("Ви програли!")

        print(f"Ваш кредит: {credit} грн")

        choice = input("Бажаєте продовжити гру? (Y/N): ").lower()
        if choice != 'y':
            break

    print("Гра завершена.")

# Запуск гри
one_armed_bandit()
import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")
