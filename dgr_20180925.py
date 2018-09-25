Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> mans_mainigais = input("Ievadi skaitli:")
Ievadi skaitli:10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigais': 10, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigais': 10, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> type(mans_mainigais)
<type 'int'>
>>> 
=============== RESTART: /home/user/RTR105/Test_1_20180925.py ===============
Ievadi skaitli:10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/Test_1_20180925.py', 'mans_mainigais': 10, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/Test_1_20180925.py ===============
Ievadi skaitli:20
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/Test_1_20180925.py', 'mans_mainigais': 20, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/Test_1_20180925.py ===============
Ievadi skaitli:5
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/Test_1_20180925.py', 'mans_mainigais': 5, '__package__': None, 'x': 25, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/Test_1_20180925.py ===============
Ievadi skaitli:
=============== RESTART: /home/user/RTR105/Test_1_20180925.py ===============
Ievadi skaitli:56
mans_mainigais = 
>>> 
=============== RESTART: /home/user/RTR105/Test_1_20180925.py ===============
Ievadi skaitli:156
mans_mainigais = 156
>>> 
=============== RESTART: /home/user/RTR105/Test_1_20180925.py ===============
Ievadi skaitli:3

Traceback (most recent call last):
  File "/home/user/RTR105/Test_1_20180925.py", line 4, in <module>
    print("mans_mainigais = %d"%(mans_mainigai))
NameError: name 'mans_mainigai' is not defined
>>> 
=============== RESTART: /home/user/RTR105/Test_1_20180925.py ===============
Ievadi skaitli:45667
mans_mainigais = 45667
>>> 
=============== RESTART: /home/user/RTR105/Test_1_20180925.py ===============
Ievadi skaitli:12
mans_mainigais = 12
vai Tu esi ievadijis skaitli: 12
vel atmina tagad ir ari mainigais x = 144
>>> 
=============== RESTART: /home/user/RTR105/Test_1_20180925.py ===============
Ievadi skaitli:45
mans_mainigais = 45
Respektivi, Tu esi ievadijis skaitli: 45
vel atmina tagad ir ari mainigais x = 2025
>>> 
=============== RESTART: /home/user/RTR105/Test_1_20180925.py ===============
Ievadi daļskaitli:8.6549
mans_mainigais =      8.655
Respektivi, Tu esi ievadijis skaitli:     8.6549
vel atmina tagad ir ari mainigais x =      74.9072940
>>> 
=============== RESTART: /home/user/RTR105/Test_1_20180925.py ===============
Ievadi daļskaitli:467
mans_mainigais =    467.000
Respektivi, Tu esi ievadijis skaitli:   467.0000
vel atmina tagad ir ari mainigais x =  218089.0000000
>>> 
=============== RESTART: /home/user/RTR105/Test_1_20180925.py ===============
Ievadi daļskaitli:1365489753.15636486
mans_mainigais = 1365489753.156
Respektivi, Tu esi ievadijis skaitli: 1365489753.1564
vel atmina tagad ir ari mainigais x = 1864562265975030272.0000000
>>> type(mans_mainigais)
<type 'float'>
>>> 
=============== RESTART: /home/user/RTR105/Test_1_20180925.py ===============
Ievadi daļskaitli:8
mans_mainigais =      8.000
Respektivi, Tu esi ievadijis skaitli:     8.0000
vel atmina tagad ir ari mainigais x =      64.0000000
>>> type(mans_mainigais)
<type 'float'>
>>> 
=============== RESTART: /home/user/RTR105/Test_1_20180925.py ===============
Ievadi simbolu rindu:gfd

Traceback (most recent call last):
  File "/home/user/RTR105/Test_1_20180925.py", line 2, in <module>
    x = mans_mainigais * mans_mainigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============== RESTART: /home/user/RTR105/Test_1_20180925.py ===============
Ievadi simbolu rindu:aaaa
mans_mainigais = aaaa
Respektivi, Tu esi ievadijis skaitli: aaaa
>>> 

