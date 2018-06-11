import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

sant = int(input("Scolko ti vesesh? "))
du = sant / 2.54
fut = 0
if du <= 12:
    print("Ti vesesh %.2f duimov" % du)
else:
    fut = sant//12
    du = sant%12
    print("Ti vesesh " + str(fut) + " futov")
    print("i %.2f duimov" % du)


printTimeStamp("iJustD")