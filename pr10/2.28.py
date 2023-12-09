def check_syntax_c(program):
    stack = []

    for char in program:
        if char == '{':
            stack.append(char)
        elif char == '}':
            if len(stack) == 0 or stack[-1] != '{':
                return False
            stack.pop()

    return len(stack) == 0

c_program = input("Введіть текст програми мовою C: ")

result = check_syntax_c(c_program)

if result:
    print("Фігурні дужки використані правильно!")
else:
    print("У тексті програми є помилки у використанні фігурних дужок.")
import datetime
def printTimeStamp(name):
  print("Автор програми: " + name)
  print("Час компіляції: " + str(datetime.datetime.now()))
printTimeStamp("Скубій Євгенія")