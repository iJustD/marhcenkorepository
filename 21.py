import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
n = int(input())
c = float(n*(n + 1)*(0.5))
print (c)
printTimeStamp("iJustD")