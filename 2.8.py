import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
day = int(input("Введите день когда вы родились: "))
month = input("Введите месяц когда вы родились(Январь,Февраль, и тд): ")
if month == 'Декабрь':
	astro_sign = 'Стрелец' if (day < 22) else 'Козерог'
elif month == 'Январь':
	astro_sign = 'Козерог' if (day < 20) else 'Водолей'
elif month == 'Февраль':
	astro_sign = 'Водолей' if (day < 19) else 'Рыбы'
elif month == 'Март':
	astro_sign = 'Рыбы' if (day < 21) else 'Овен'
elif month == 'Апрель':
	astro_sign = 'Овен' if (day < 20) else 'Телец'
elif month == 'Май':
	astro_sign = 'Телец' if (day < 21) else 'Близнецы'
elif month == 'Июнь':
	astro_sign = 'Близнецы' if (day < 21) else 'Рак'
elif month == 'Июль':
	astro_sign = 'Рак' if (day < 23) else 'Лев'
elif month == 'Август':
	astro_sign = 'Лев' if (day < 23) else 'Дева'
elif month == 'Сентябрь':
	astro_sign = 'Дева' if (day < 23) else 'Весы'
elif month == 'Октябр':
	astro_sign = 'Весы' if (day < 23) else 'Скорпион'
elif month == 'Ноябрь':
	astro_sign = 'Скорпион' if (day < 22) else 'Стрелец'
print("Ваш знак зодиака :",astro_sign)
printTimeStamp("iJustD")