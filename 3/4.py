import datetime
def printTimeStamp(name):
    print('iJustD: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


chisla = []
n = int(input("Vvedite chislo: ")) + 1

for i in range(0, n):
    chisla.append(i)

chisla.remove(0)
chisla.remove(1)
p = 2
while p < n:
    for i in chisla:
        if i % p == 0 and i != p:
            chisla.remove(i)
    p += 1

print(chisla)


