'''
Exception Creation

1. Custom Exception, (raise)
2. User-defined Exception, (raise)
3. Assertion Exception, (assert)

'''

'''
Custom exception:
  1. we use pre-built Exception classes according to our requirement.


  --> raise ValueError('message')

  --> ValueError: message

'''

# num = 17
# if num >= 18:
#     print('You are eligible for voting and driving')
# else:
#     raise ValueError('Age should be Greater than or equals to 18!')  



'''
-- User-defined Exception:

  1. It is a type of exception in which we can create our own exception classes bassed upon our own requirement. We can also provide names to
  those classes according the user cases.

'''

# class MyException(Exception):
#     pass

# raise MyException('This is my exception class!')

# n1, n2 = 10, 0

# if n2 == 0:
#     raise MyException("Second number can't be zero")

# else:
#     print(n1/n2)



'''
Assertion Exception:
  -- It can be created one keyword called 'assert'


assert <condition>, print(ERROR)--->if condition is False
print(output) ---> if condition is true

'''

s = input('Enter a String:')
assert s == s[::-1], print('It is not a palindromic string')
print('It is a palindrominc string')


