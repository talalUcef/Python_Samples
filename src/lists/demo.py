'''
Created on 2 août 2015

@author: talalUcef
'''

# declare new List
ints = [10, 20, 30, 40, 50]
chars = ['a', 'b' , 'c', 'd']
string = ["toto", "tata", "titi"]
hybrid = [1, 2.0, "toto", ['t', 'o', 't', 'o']]
print(ints)

#Read list
def print_l (my_list) :
    for item in my_list :
        print(item)
     
def update_l(my_list, current_value, new_value) :
    for i in range(len(my_list)) :
        if my_list[i] == current_value :
            my_list[i] = new_value
            break
        
print_l(ints)
print_l(chars)
print_l(string)
print_l(hybrid)

update_l(ints, 50, 100)
print_l(ints)
