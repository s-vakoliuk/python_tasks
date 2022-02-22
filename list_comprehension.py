"""
list comprehension

1) Дано рядок:
greeting = 'Hello, world'
записати кожен символ в список замінивши його верхний регістр
Приклад:
['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
"""

# greeting = 'Hello, world'
# greeting = greeting.upper()
# listOfLetters = list(greeting)
# print(listOfLetters)

"""
2) З діапазону від 0 до 50 записати в список тільки не парні числа, при цьому піднести їх до квадрату
пример:
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
"""

listOfNumbers=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,48,49,50]

# listOfNumbers2=[]
# for i in listOfNumbers:
#     listOfNumbers2.append(i ** 2)

listOfNumbers2= [(i ** 2)for i in listOfNumbers]
print(listOfNumbers2)