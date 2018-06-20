import datetime
def printTimeStamp(name):
    print('iJustd: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

t = open("minecraft.txt", 'a')
t.write("\n\nPifagor F.P.")

t.close()


