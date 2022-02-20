"""
Tasks with decorators
- є функція:
def pr():
    return 'Hello_boss_!!!'
 написати декоратор до цієї функції, який замінює нижні підкреслення на пробіли і повертає це значення
"""

def decor(func):
    def wrap():
        return func().replace('_', ' ')
    return wrap

@decor
def pr():
    return (input("Enter words with: "))

print(pr())