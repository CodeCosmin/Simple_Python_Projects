print("---------- SIRUL LUI FIBONACCI ----------")
def sirul_lui_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return n
    else:
        return sirul_lui_fibonacci(n-1) + sirul_lui_fibonacci(n-2)
    
number = int(input("Ce lungime doriti sa aiba sirul lui Fibonacci?: "))
for i in range(1, number):
    print(sirul_lui_fibonacci(i), end=" ")