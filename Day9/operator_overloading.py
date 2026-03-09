'''
-- Operator Overloading: It is a phenomemon of makeing the operators to work on user-defined data types by invoking respective magic methods.

-- Magic Method/Dundar: It is a special type of methods in which double underscores will be there at the starting & ending of the mnethod's name.

-- Example:
    1. __add__,
    2. __sub__,
    3. __mul__,
    4. __floordiv__,
    5. __truediv__,
    6. __mod__,
    
-- If we don't use operator overloading then what will happen ?
    For using the operators inside user-defined data types we have to use operator overloading.

-- Syntax:
    class ClassName:
        def __init__(self, val):
            self.val = val
        
        def __add__(self, ano_obj):
            return self.val + ano_obj.val
    
    obj1 = ClassName(val1)
    obj2 = ClassName(val2)
    print(obj1 + obj2)  ## obj1.__add__(obj2)
'''


class MyDT:
    def __init__(self, val):
        self.val = val
    
    def __str__(self):
        return str(self.val)
    
    def __add__(self, *ano_obj):
        sum = self.val
        for i in ano_obj:
            sum += i.val
        return MyDT(sum)
    
    def __sub__(self, ano_obj):
        return self.val - ano_obj.val
    
    def __mul__(self, ano_obj):
        return self.val * ano_obj.val
    
    def __floordiv__(self, ano_obj):
        return self.val // ano_obj.val
    
    def __truediv__(self, ano_obj):
        return self.val / ano_obj.val
    
    def __mod__(self, ano_obj):
        return self.val % ano_obj.val

# add = MyDT(100) + MyDT(200) + MyDT(300) + MyDT(400) + MyDT(500)
# print(MyDT.add(MyDT(100), MyDT(200), MyDT(300), MyDT(400), MyDT(500)))
print(MyDT(10) + MyDT(20))

print(MyDT(100) - MyDT(20))
print(MyDT(10) * MyDT(20))
