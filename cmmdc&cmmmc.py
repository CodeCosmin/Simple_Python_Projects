print("---------- CEL MAI MARE DIVIZOR COMUN SI CEL MAI MIC MULTIPLU COMUN ----------")
def cmmdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def cmmmc(a, b):
    return abs(a * b) // cmmdc(a, b)

number1 = int(input("Va rugam introduceti primul numar: "))
number2 = int(input("Va rugam introduceti primul numar: "))
print(f"Cel mai mare divizor comun al lui {number1} si {number2} este: {cmmdc(number1, number2)}")
print(f"Cel mai mic multiplu comun al lui {number1} si {number2} este: {cmmmc(number1, number2)}")