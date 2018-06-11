import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
print('Your name')
name = input()
print('Helo, ' + name + '!')

printTimeStamp("iJustD")