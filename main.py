def summa(a, b):
    return a + b

def raznost(a, b):
    return a - b

def umnojenie(a, b):
    return a * b

def delenie(a, b):
    return a // b

operation = input("Введите операцию(+, -, *, /): ")
res = None

if operation == "+":
    res = summa(int(input("Введите 1 число: ")), int(input("Введите 2 число: ")))

elif operation == "-":
    res = raznost(int(input("Введите 1 число: ")), int(input("Введите 2 число: ")))

elif operation == "*":
    res = umnojenie(int(input("Введите 1 число: ")), int(input("Введите 2 число: ")))

elif operation == "/":
    res = delenie(int(input("Введите 1 число: ")), int(input("Введите 2 число: ")))

else:
    print("Неверная операция")

print("Результат оперции:",res)