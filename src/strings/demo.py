'''
Created on 2 août 2015

@author: talalUcef
'''

# String are sequence of characters
fruit = "banana"
letter = fruit[0]
print("First letter "+ letter)

# len Function
length = len(fruit)
print("Fruit lenth "+ length.__str__())

# Get the lase Element
print("Last letter "+ fruit[length - 1])

# Traversal with a while loop
print("Tracersal with a while loop ")
index = 0
while index < len(fruit) :
    print(fruit[index])
    index = index + 1
 
print("Tracersal with a for loop ")   
# Ttaversal with a for loop
for letter in fruit :
    print(letter)
   
# String slice
full_nme = "firs_name last_name"
first_name = full_nme[0:9]
print("First name : "+first_name) 

# Upper method
print("First name in upper case : "+first_name.upper())

    

