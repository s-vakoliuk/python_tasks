# Створити функцію котра приймає число і повертає так, як в прикладі.
# Наприклад: ввели 3275, а виведе "3000 + 200 + 70 +5"

def bitNumber (number):
    number = str(number)
    listOfNumbers = list(number)  # Переведення в список рядків

    reverselistOfNumbers = listOfNumbers[::-1]  # Формуємо зворотній список чисел

    result = []
    for index, value in enumerate(reverselistOfNumbers):
        count = index + 1
        if index == 0:
           value = value
        else:
            count = index+1
            value = value+("0"*count)
        result.append(value)

    result[::-1] = result
    resultString = "+".join(result) # З'єднуємо елементи списку знаком "+"
    return print("Результат рядка: ", resultString)

bitNumber(3275)