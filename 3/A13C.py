import datetime
def printTimeStamp(name):
    print('iJustD: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))



def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n

print(fac(5))

