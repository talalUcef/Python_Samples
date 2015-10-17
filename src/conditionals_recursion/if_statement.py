# if Statement
x = 1
if x == 1 :
    print("x equals 1")
    
# function is_even
def is_even(num):
    if num % 2 == 0 :
        print(str(num)+" is even")
    else :
        print(str(num)+" is odd")

is_even(4)
is_even(5)

def countdown(n):
    if n <= 0:
        print ("Blastoff !")
    else:
        print(n)
        countdown(n-1)
        
countdown(10)

def factorial (n):
    if not isinstance(n, int):
        print ("Factorial is only defined for integers.")
        return None
    elif n < 0:
        print ("Factorial is not defined for negative integers.")
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
factorial("toto")
factorial(3.2)
print(factorial(5))