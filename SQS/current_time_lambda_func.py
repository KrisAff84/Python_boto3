import boto3
import json
import time

current_time = []
t = time.localtime()
c_time = time.strftime('%a:%m:%d:%I:%M:%S:%p')
current_time.append(c_time.split(':'))

day = current_time[0][0]
month = current_time[0][1]
date = current_time[0][2]
hour = current_time[0][3]
minutes = current_time[0][4]
seconds = current_time[0][5]
am_pm = current_time[0][6]

print(f'The current date and time is:')
print(day, month, date + ',',hour + ':' + minutes + ':' + seconds, am_pm)