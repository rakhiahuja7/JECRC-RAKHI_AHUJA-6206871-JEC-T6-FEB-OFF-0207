'''
its a type of inheritance in which the properties will be derived from 
one to another class by considering more than one level it is multilevel inheritance.
it is also called sequential inheritance.
'''
class Class_1: ##Parent class or, Super class of class_2
    a="class_1"

class Class_2(Class_1): ##Child class or, Sub class of class_1, parent class or, Super class of class_3
    b="class_2"

class Class_3(Class_2): ##Child class or, Sub class of class_2, parent class or, Super class of class_4
    c="class_3"

class Class_4(Class_3): ##Child class or, Sub class of class_3, parent class or, Super class of class_5
    d="class_4"

class Class_5(Class_4): ##Child class or, Sub class of class_4, parent class or, Super class of class_6
    e="class_5"

obj=Class_5()
print(obj.a, obj.b, obj.c, obj.d, obj.e) ## by using class_5 object we can access the properties of all the classes in the hierarchy
