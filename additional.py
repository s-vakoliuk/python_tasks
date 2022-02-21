# Створити функцію котра приймає число і повертає так, як в прикладі.
# Наприклад: ввели 3275, а виведе "3000 + 200 + 70 +5"

number = (input("Введіть число: "))
print("Введене число: ", number)
count=len(number)
print("Кількість цифр: ", count)

listOfNumbers = list(number) # переведення в список рядків
print("Список рядків", listOfNumbers)

for item in range(len(listOfNumbers)):
    listOfNumbers[item]=int(listOfNumbers[item])
print("Список чисел", listOfNumbers)

reverselistOfNumbers=listOfNumbers[::-1]
print("Зворотній список чисел", reverselistOfNumbers)

result=[]
for index, value in enumerate(reverselistOfNumbers):
    result.append(value * (10**index))

print("Результат списку чисел", result)

result[::-1] = [str(i) for i in result] # переведення списку чисел в список рядків
print("Результат списку рядків", result)
resultString = "+".join(result)
print(resultString)