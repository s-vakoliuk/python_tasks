# Створити функцію котра приймає число і повертає так, як в прикладі.
# Наприклад: ввели 3275, а виведе "3000 + 200 + 70 +5"

# number = (input("Введіть число: "))
# print("Введене число: ", number)
# count=len(number)
# print("Кількість цифр: ", count)
#
# listOfNumbers = list(number) # Переведення в список рядків
# print("Список рядків", listOfNumbers)
#
# for item in range(len(listOfNumbers)):
#     listOfNumbers[item]=int(listOfNumbers[item])
# print("Список чисел", listOfNumbers)
#
# reverselistOfNumbers=listOfNumbers[::-1] # Формуємо зворотній список чисел
#
# result=[]
# for index, value in enumerate(reverselistOfNumbers):
#     result.append(value * (10**index))
# print("Результат списку чисел", result)
#
# result[::-1] = [str(i) for i in result] # Переведення списку чисел в список рядків
# resultString = "+".join(result)
# print("Результат списку рядків", resultString)

#########################################################

def bitnumber (number):
    number=str(number)
    listOfNumbers = list(number)  # Переведення в список рядків

    for item in range(len(listOfNumbers)):
        listOfNumbers[item] = int(listOfNumbers[item])

    reverselistOfNumbers = listOfNumbers[::-1]  # Формуємо зворотній список чисел

    result = []
    for index, value in enumerate(reverselistOfNumbers):
        result.append(value * (10 ** index)) # Кожному елементу масиву множимо на (10 ** index)

    result[::-1] = [str(i) for i in result]  # Переведення списку чисел в список рядків
    resultString = "+".join(result) # З'єднуємо числа знаком "+"
    return print("Результат рядка: ", resultString)

bitnumber(3275)