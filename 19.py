import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
import datetime
b = datetime.datetime.now()
print(b)
printTimeStamp("iJustD")