import random 
number = random.randint(1, 10)
while True:
    user_number = int(input("Va rugam introduceti un numar de la 1 la 10: "))
    if user_number >= 1 and user_number <= 10:
        if user_number == number:
            print("Felicitari, ati ghicit numarul !!!")
        else:
            print("Numar gresit, incercati din nou")
            continue
    else:
        print("Numarul este in afara intervalului, va rugam incercati din nou !!!")
        continue
    choice = input("Doriti sa mai ghiciti un numar?(y/n): ")
    if choice == 'y':
        continue
    elif choice == 'n':
        break