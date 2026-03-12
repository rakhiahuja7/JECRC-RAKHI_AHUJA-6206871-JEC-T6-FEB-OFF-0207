import time

'''
Exception Handling Approaches

---> Specific Exception Handling
---> Generic Exception Handling
---> Default Exception Handling

'''


'''
Specific Exception Handling :
 
--> If we are aware of the error or the exception the we can go with "Specific"

try:
    problem Statement

except ErrorName:
    resolution/
    solution code

'''

# n1, n2 = 21, 0
# # result = n1 / n2
# # print(result)
# try:
#     ## Problem Statement
#     result = n1 / n2
#     print(result)

# except ZeroDivisionError:
#     ## Solution Code
#     print('Please do not choose 0 as the second number!')

# print('Code after try except 01')
# print('Code after try except 02')  

# try:
#     a, b, c = 1, 2
    
# except ValueError:
#     print('For performing MVC, no. of variables should be equal to no. of values!')  

# try:
#     print(a, b, c)

# except NameError:
#     print('Identifiers are not their in the memory!')



'''
Generic Exception Handling 

It is a type of exception handling approach in which there is no need to pass any particular exception class name. Instead we can use parent 'exception'
class called "Exception".
-- Using "Generic Exception Hnadling", we can't handle keyword interruption.

'''

# try:
#     a, b, c = 1, 2
    
# except Exception:
#     print('For performing MVC, no. of variables should be equal to no. of values!')  

# try:
#     print(a, b, c)

# except Exception:
#     print('Identifiers are not their in the memory!')


#3 keyboardInterruption 
# try:
#     while True:
#         print(time.time())
# except Exception:
#     print('Loop Stopped!!')   

## keyboradInterrupt by using Specific
# try:
#     while True:
#         print(time.time())
# except KeyboardInterrupt:
#     print('Loop Stopped!!') 


'''
Default Exception Handling 
'''

import time

'''
Exception Handling Approaches

---> Specific Exception Handling
---> Generic Exception Handling
---> Default Exception Handling

'''


'''
Specific Exception Handling :
 
--> If we are aware of the error or the exception the we can go with "Specific"

try:
    problem Statement

except ErrorName:
    resolution/
    solution code

'''

# n1, n2 = 21, 0
# # result = n1 / n2
# # print(result)
# try:
#     ## Problem Statement
#     result = n1 / n2
#     print(result)

# except ZeroDivisionError:
#     ## Solution Code
#     print('Please do not choose 0 as the second number!')

# print('Code after try except 01')
# print('Code after try except 02')  

# try:
#     a, b, c = 1, 2
    
# except ValueError:
#     print('For performing MVC, no. of variables should be equal to no. of values!')  

# try:
#     print(a, b, c)

# except NameError:
#     print('Identifiers are not their in the memory!')



'''
Generic Exception Handling 

It is a type of exception handling approach in which there is no need to pass any particular exception class name. Instead we can use parent 'exception'
class called "Exception".
-- Using "Generic Exception Hnadling", we can't handle keyword interruption.

'''

# try:
#     a, b, c = 1, 2
    
# except Exception:
#     print('For performing MVC, no. of variables should be equal to no. of values!')  

# try:
#     print(a, b, c)

# except Exception:
#     print('Identifiers are not their in the memory!')


#3 keyboardInterruption 
# try:
#     while True:
#         print(time.time())
# except Exception:
#     print('Loop Stopped!!')   

try:
    while True:
        print(time.time())
except KeyboardInterrupt:
    print('Loop Stopped!!') 


'''
Default Exception Handling 
'''


import time

'''
Exception Handling Approaches

---> Specific Exception Handling
---> Generic Exception Handling
---> Default Exception Handling

'''


'''
Specific Exception Handling :
 
--> If we are aware of the error or the exception the we can go with "Specific"

try:
    problem Statement

except ErrorName:
    resolution/
    solution code

'''

# n1, n2 = 21, 0
# # result = n1 / n2
# # print(result)
# try:
#     ## Problem Statement
#     result = n1 / n2
#     print(result)

# except ZeroDivisionError:
#     ## Solution Code
#     print('Please do not choose 0 as the second number!')

# print('Code after try except 01')
# print('Code after try except 02')  

# try:
#     a, b, c = 1, 2
    
# except ValueError:
#     print('For performing MVC, no. of variables should be equal to no. of values!')  

# try:
#     print(a, b, c)

# except NameError:
#     print('Identifiers are not their in the memory!')



'''
Generic Exception Handling 

It is a type of exception handling approach in which there is no need to pass any particular exception class name. Instead we can use parent 'exception'
class called "Exception".
-- Using "Generic Exception Hnadling", we can't handle keyword interruption.

'''

# try:
#     a, b, c = 1, 2
    
# except Exception:
#     print('For performing MVC, no. of variables should be equal to no. of values!')  

# try:
#     print(a, b, c)

# except Exception:
#     print('Identifiers are not their in the memory!')


#3 keyboardInterruption 
# try:
#     while True:
#         print(time.time())
# except Exception:
#     print('Loop Stopped!!')   




'''
Default Exception Handling

-- It is a type of exception handling in which we can handle all type of errors or exception except 'SyntaxError'

'''

try:
    while True:
        print(time.time())
except:
    print('Loop Stopped!!') 
