'''
its a type of inheritance in which the properties will be derived from multiple parent 
classes to a single child class.
'''
class Parent_1:
    a = "Parent_1"
class Parent_2:
    b = "Parent_2"
class Parent_3:
    c = "Parent_3"
class Parent_4:
    d = "Parent_4"
class Child(Parent_1, Parent_2, Parent_3, Parent_4):
    pass

obj = Child()
print(obj.a, obj.b, obj.c, obj.d) ## by using child class object we can access the properties of all the parent classes
