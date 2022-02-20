"""
Tasks with strings

1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
наприклад:
st = 'as 23 fdfdg544' введена строка
2,3,5,4,4        #вивело в консолі.
"""

# string = "as 23 fdfdg544"
# print("Заданий рядок ", string)
# num = ""
# for count in string:
#     if count.isdigit():
#         num = num + count
# print("Виведення цифр з рядка: " + num)

"""2)написати прогу яка вибирає зі введеної строки числа і виводить їх так як вони написані
наприклад:
  st = 'as 23 fdfdg544 34' #введений рядок
  23, 544, 34              #виведення в консолі
"""

string = 'as 23 fdfdg544 34'
print("Заданий рядок ", string)
for char in string:
    if char in "asfddg":
        string = string.replace(char, '')
print (string)