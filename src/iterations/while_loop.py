'''
Created on 2 août 2015

@author: talalUcef
'''
def countdown(n):
    while n > 0:
        print(n)
        n = n-1
    print ("Blastoff!")
    
countdown(3)

def sequence(n):
    while n != 1:
        print(n)
        if n%2 == 0: # n is even
            n = n/2
        else: # n is odd
            n = n*3+1
sequence(3)