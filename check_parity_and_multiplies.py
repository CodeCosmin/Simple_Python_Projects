print("---------- VERIFICARE PARITATE SI MULTIPLII ----------")
while True:
    number = int(input("Va rugam introduceti un numar: "))
    if number % 2 == 0:
        print("Acest numar este par si multiplu lui 2")
    else:
        print("Acest numar este impar si nu este multiplu al lui 2")
    if number % 3 == 0 and number % 5 == 0:
        print("Acest numar este multiplu de al lui 3 si al lui 5")
    elif number % 3 == 0:
        print("Acest numar este multiplu de al lui 3 dar nu al lui 5")
    elif number % 5 == 0:
        print("Acest numar este multiplu de al lui 5 dar nu al lui 3")
    else:
        print("Acest numar nu este multiplu de al lui 3 sau al lui 5")
    choice2 = input("Doriti sa mai verificati un alt numar?(y/n): ")
    if choice2 == 'y':
        continue
    else:
        break