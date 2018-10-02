Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> xx =2
>>> xx = xx + 2
>>> print (xx)
4
>>> x = 1 + 2 ** 3 / 4 * 5
>>> print(x)
11
>>> 5 / 4.
1.25
>>> 5/4
1
>>> a =5
>>> b=4
>>> c =
SyntaxError: invalid syntax
>>> c = ?
SyntaxError: invalid syntax
>>> c=a/b
>>> ee="hello"+"world"
>>> print(ee)
helloworld
>>> ee="hello "+"world"
>>> print(ee)
hello world
>>> x=1
>>> type(x)
<type 'int'>
>>> temp = 9.5
>>> type(temp)
<type 'float'>
>>> print(10/2)
5
>>> int(132.5648)
132
>>> int(132.9648)
132
>>> sval='123'
>>> type(sval)
<type 'str'>
>>> print(sval + 1)

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(sval + 1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival = int(sval)
>>> type (ival)
<type 'int'>
>>> print (ival + 1)
124
>>> nam = input('Who are you?')
Who are you?bob

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    nam = input('Who are you?')
  File "<string>", line 1, in <module>
NameError: name 'bob' is not defined
>>> print('Welcome',nam)

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print('Welcome',nam)
NameError: name 'nam' is not defined
>>> nam = input('Who are you?')
Who are you?

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    nam = input('Who are you?')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> nam = raw_input('Who are you?')
Who are you? Dima
>>> print("Welcome",nam)
('Welcome', ' Dima')
>>> inp = input("Europe floor?")
Europe floor?0
>>> usf = int(inp) + 1
>>> print("US floor",usf)
('US floor', 1)
>>> 
