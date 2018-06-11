import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

time = [22, 23, 24, 1, 2, 3, 4, 5, 6, 7, 8]

papu = input("+ esli papuga govorit, else - ")
my_time = int(input("A scolco vremeni? "))
if papu == '-':
    print("Tak, raz papuga molchit tak i ti molchi")
elif papu == '+' and my_time not in time:
    print("Sechas den, ne trogai menia")
else:
    print("Nakroi papugu kletkoi")


printTimeStamp("iJustD")