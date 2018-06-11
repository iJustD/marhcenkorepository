import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

dni = int(input("Scolko dnei "))
god = int(input("Scolko godin "))
hv = int(input("Scolko hvilin "))
sec = int(input("Scolko secund "))

all_time = dni * 24 * 60 * 60 + god * 60 * 60 + hv * 60 + sec
print("Ti putishestvoval " + str(all_time) + " secund")


printTimeStamp("iJustD")