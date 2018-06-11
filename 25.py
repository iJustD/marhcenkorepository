import datetime

mytime = '08:17:45:38'
time_delta = datetime.datetime.now() - datetime.datetime.strptime(str(mytime), '%d %H:%M:%S')
print(time_delta.total_seconds())
