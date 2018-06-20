import datetime
def printTimeStamp(name):
    print('ijustD: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))



def hotel(days, price):
    return days * price

def travel(city):
    if city == "Черкаси":
        return 100
    elif city == "Київ":
        return 1000

def car(day):
    summ = day * 20
    if day >= 7:
        summ -= 25
    elif 3 < day < 7:
        summ -= 10
    return summ

def calculate(day, city, money):
    must_pay = travel(city) + hotel(day, 200) + car(day) + money
    return must_pay

print(calculate(10, "Черкаси", 1000))


