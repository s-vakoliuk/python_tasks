# Створити функцію котра приймає число і повертає так, як в прикладі.
# Наприклад: ввели 3275, а виведе "3000 + 200 + 70 +5"

def bit_number(number):
    number = str(number)
    list_of_numbers = list(number)  # Переведення в список рядків

    reverse_list_of_numbers = list_of_numbers[::-1]  # Формуємо зворотній список чисел

    result = []
    for index, value in enumerate(reverse_list_of_numbers):
        count = index
        if value !="0":
            value = value+("0"*count)
            result.append(value)

    result[::-1] = result
    result_string = "+".join(result) # З'єднуємо елементи списку знаком "+"
    return print("Результат рядка: ", result_string)

bit_number(300502700501)