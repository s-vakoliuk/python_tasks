"""Написати функцію на замикання, яка буде в собі зберігати список справ.
Вам потрібно реалізувати два методи:
- перший записує в цю змінну запис
- другий повертає всі записи

запишіть 5 справ
виведіть весь список справ"""

def notebook():
    todo_list = []

    def add_todo(new_todo):
        nonlocal todo_list
        todo_list.append(new_todo)

    def get_all():
        return todo_list

    return {'add_todo': add_todo, 'get_all': get_all}

add_todo, get_all = notebook()

while True:
    for item in range (5):
        add_todo = str(input("Enter the case in the to-do list: "))
    break

print(get_all())
