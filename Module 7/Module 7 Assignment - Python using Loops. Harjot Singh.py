Python 3.11.3 (v3.11.3:f3909b8bc8, Apr  4 2023, 20:12:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> list = []
>>> for i in range(15):
...     list.append(random.randint(1, 100))
... 
...     
>>> for i in range(len(list)):
...     if list[i] % 2 == 0:
...         print(f"{i + 1}: {list[i]} is even")
...     else:
...         print(f"{i + 1}: {list[i]} is odd")
... 
...         
1: 85 is odd
2: 26 is even
3: 91 is odd
4: 28 is even
5: 7 is odd
6: 15 is odd
7: 44 is even
8: 57 is odd
9: 9 is odd
10: 8 is even
11: 25 is odd
12: 72 is even
13: 17 is odd
14: 25 is odd
15: 84 is even
