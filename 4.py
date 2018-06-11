import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

latters = ['a', 'e', 'i', 'o', 'u']
user = input("Введіть букву ")
if user in latters:
    print("Ваша буква голосна")
elif user == 'y':
    print("Ваша буква може бути і голосною і приголосною")
else:
    print("Ваша буква приголосна")

printTimeStamp("iJustD")