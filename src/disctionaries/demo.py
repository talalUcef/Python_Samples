'''
Created on 2 août 2015

@author: talalUcef
'''

# new dictionary
eng2sp = dict()
print("values of eng2sp "+eng2sp.__str__())

eng2sp["one"] = "uno"
print("values of eng2sp "+eng2sp.__str__())

# new dictionary 
eng2sp = {' one' : ' uno' , ' two' : ' dos' , ' three' : ' tres' }
print("values of eng2sp "+eng2sp.__str__())

# Traversal disctionary
def read_dict(d):
    for key in d :
        print("(", key, ",", d[key], ")")
        
read_dict(eng2sp)
