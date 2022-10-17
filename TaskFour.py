print("\033c")

numb = int(input("Введите число для перевода в двоичную систему исчисления: "))
answer = ""

while numb > 0:
    temp = str(numb % 2)
    answer = temp + answer
    numb = int(numb / 2)

print(f"Ответ: {answer}")