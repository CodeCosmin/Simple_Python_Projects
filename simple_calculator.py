print("---------- CALCULATOR SIMPLU ----------")
while True:
    number1 = int(input("Va rugam introduceti primul numar: "))
    number2 = int(input("Va rugam introduceti primul numar: "))
    op = ['+', '-', '*', '/']
    operatie = input("Va rugam introduceti operatia de calcul pe acre doriti sa o faceti(+ - * /): ")
    if operatie in op:
        if operatie == '+':
            rezultat = number1 + number2
            print("Rezultatul este:",rezultat)
        elif operatie == '-':
            rezultat = number1 - number2
            print("Rezultatul este:",rezultat)
        elif operatie == '*':
            rezultat = number1 * number2
            print("Rezultatul este:",rezultat)
        else:
            if number2 == 0:
                print("Operatia nu are sens!!!")
            else:
                rezultat = number1 / number2
                print("Rezultatul este:",rezultat)
    else:
        print("Aceasta operatie nu este disponibila, va rugam incercati din nou: ")
    choice = input("Doriti sa mai faceti o operatie de calcul?(y/n): ")
    if choice == 'y':
        continue
    else:
        break