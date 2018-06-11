import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

chtoto1 = int(input("Scolco shtucjk ti kupil "))
chtoto2 = int(input("Scolco shtukovin ti kupil "))

print("V obschem ti budesh nesti " + str(chtoto1 * 75 + chtoto2 * 112) + " gram")


printTimeStamp("Pifagor")