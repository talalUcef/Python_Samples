'''
Created on 2 août 2015

@author: talalUcef
'''
# function without parameter
def print_lyrics():
    print("I' m a lumberjack, and I' m okay.")
    print("I sleep all night and I work all day.")
          
print("call funnction print_lyrics()")
print_lyrics()

# dunction with parameter
def print_twice(name):
    print(name)
    print(name)
    
print("call funnction print_twice(name)")
print_twice("Tallal")

# function with parameter and return statment
def calcul_sqrt(num):
    return num*num
print("The sqrt of 2 : "+ str(calcul_sqrt(2)))

