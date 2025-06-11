import random

print("---------- GENERATOR DE PAROLE ----------")
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
caracters = ",.<>;:[}]{|/?~`!@#$%^&*()_+=-"

while True:
    lungime = int(input("Va rugam sa specificati lungimea parolei: "))
    choice1 = input("Doriti ca parola sa contina si cifre?(y/n): ")
    if choice1 == 'y':
        choice2 = input("Doriti ca parola sa contina si caractere speciale?(y/n): ")
        if choice2 == 'y':
            parola = letters + numbers + caracters
            password = ''.join(random.choice(parola) for _ in range (lungime))
            print("Parola dumneavoastra este:",password)
        else:
            choice3 = input("Doriti ca parola sa contina doar cifre si caractere speciale?(y/n): ")
            if choice3 == 'y':
                parola = numbers + caracters
                password = ''.join(random.choice(parola) for _ in range (lungime))
                print("Parola dumneavoastra este:",password)
            else:
                parola = letters + numbers
                password = ''.join(random.choice(parola) for _ in range (lungime))
                print("Parola dumneavoastra este:",password)
    else:
        password = ''.join(random.choice(letters) for _ in range (lungime))
        print("Parola dumneavoastra este:",password)
    choice_final = input("Doriti sa mai generati inca o parola?(y/n): ")
    if choice_final == 'y':
        continue
    else:
        break