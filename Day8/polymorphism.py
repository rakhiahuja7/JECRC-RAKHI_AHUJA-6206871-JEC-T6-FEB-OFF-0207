'''
Polymorphism is using the same method name or operator to perform two or more 
different operators
class Temp:
    def sum(self,a,b):
        print(a+b)

    add_two_nums=sum

    def sum(self,a,b,c):
        print(a+b+c)

in python if we want to perform method overloading then it will act as method overriding 
in other progtamming languages based upon no of arguments, the respective method block 
will be executed but in python it never happens.

method overriding is a phenomenon of overriding the prev method's address eith the latest one

'''
class Temp:
    def sum(self,a,b):
        print(a+b)
    #monkey patching :- it is a process of storing the prev method's address inside a variable before overriding the 
    # method area's address. using that var, we can access the prev method's method area.
    add_two_nums=sum
    
    def sum(self,a,b,c):
        print(a+b+c)

obj=Temp()
obj.sum(1,2,3) ## it will execute the latest method block
obj.add_two_nums(1,2) ## it will also execute the latest method block because add_two_nums is also pointing to the latest method block
#obj.sum(1,2,3)
