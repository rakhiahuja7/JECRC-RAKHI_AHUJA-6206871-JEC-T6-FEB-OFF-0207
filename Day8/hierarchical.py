'''
its a type of inheritance in which the properties will be derived from one parent class
 to multiple child classes.
'''
class Parent:
    gold = "2Kg"
    silver = "5Kg"
    no_of_flats = 3

class Child_1(Parent):
    name='Rickon'

class Child_2(Parent):
    my_name='BRob'

class Child_3(Parent):
    sis_name = "Sansa"

print(Child_1.gold, Child_2.silver, Child_3.no_of_flats)
