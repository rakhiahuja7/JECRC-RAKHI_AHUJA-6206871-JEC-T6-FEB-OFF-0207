'''
Encapsulation:
    1. It is used to provide security to the data(data means variables/prop & methods present inside a class).

How to provide security to the data ?
    To provide security, we have to use access specifiers.
        1. public,
        2. protected(Soft Barrier '_'),
        3. private,
        
Access Specifier:
    It described who can access the class members(properties & methods).
'''



## Example for public access specifier.
# class Temp:
#     a,b,*c,d = 'HELLO'
    
#     def greeting(self):
#         print('Good Afternoon user :)')

# class C2(Temp):
#     pass



## Protected Access Specifier
# class Temp:
#     ## Soft Barrier
#     _a = 10
#     _b = 'I LOVE PYTHON !'

# obj = Temp()
# print(obj._b)
# print(obj._a)




## Private

# class Temp:
#     __a = 100
    
#     def __status(self):
#         print('Class name is Temp!')

# obj = Temp()
# print(obj.__a)
# obj.__status()


'''
1. By using Syntax,
2. get & set method,
3. by using @property decorater(setter)
'''
## By using Syntax
'''
obj_name/class_name._CN__prop_name/__method_name (Accessing)
obj_name/class_name._CN__MemberName = new_method (Modifing)
'''
# print(obj._Temp__a) ## 100 --> '0123456789'
# print(Temp._Temp__a)
# obj._Temp__status()

# def new_method():
#     print('Method definition got changed!')

# obj._Temp__a = '0123456789'
# obj._Temp__status = new_method
# print(obj._Temp__a)
# obj._Temp__status()



## By using get & set method
# class Temp:
#     __a = 100
    
#     def __status(self):
#         print('Class name is Temp!')
#     def get(self):
#         print(self.__a)
#     def set(self, new_val):
#         self.__a = new_val
    

# obj = Temp()
# obj.get()
# obj.set(1)
# obj.get()
# print(obj._Temp__a)


## By using @property decorator
class Temp:
    __a = 10
    @property
    def get(self):
        print(self.__a)
    @get.setter
    def set(self, new_val):
        self.__a = new_val

obj = Temp()
obj.get
obj.set = 10000
obj.get
print(obj._Temp__a)
