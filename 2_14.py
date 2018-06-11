import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
year = int(input("Введите год: "))
if (year) % 12 == 0:
    sign = 'Дракон'
elif (year) % 12 == 1:
    sign = 'Змея'
elif (year) % 12 == 2:
    sign = 'Лошадь'
elif (year - 2000) % 12 == 3:
    sign = 'Овца'
elif (year - 2000) % 12 == 4:
    sign = 'Обезьяна'
elif (year - 2000) % 12 == 5:
    sign = 'Петух'
elif (year - 2000) % 12 == 6:
    sign = 'Собака'
elif (year - 2000) % 12 == 7:
    sign = 'Свинья'
elif (year - 2000) % 12 == 8:
    sign = 'Крыса'
elif (year - 2000) % 12 == 9:
    sign = 'Бык'
elif (year - 2000) % 12 == 10:
    sign = 'Тигр'
else:
    sign = 'Заяц'

print("Ваше животное :",sign)
printTimeStamp("iJustD")