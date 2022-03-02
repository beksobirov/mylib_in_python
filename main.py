import mylib

name = mylib.display('Og`abek')
print(name)

#Import only function or ... from library  
from mylib import dict
print(dict['surname'], dict['age'])