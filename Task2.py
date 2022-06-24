"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

import csv
phone_times = dict()
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls: #phone number must be unique, or value must be larger than the one listed(which means the phone number must already be listed)
        #call[0] => number
        #call[3] => duration
        if call[0] not in phone_times.keys() or (call[0] in phone_times.keys() and phone_times[call[0]] < call[3]):
            phone_times[call[0]] = call[3]
    
max_time = 0
number_associated_with_max_time = str
for number, time in phone_times.items():
    if max_time < int(time):
        max_time = int(time)
        number_associated_with_max_time = number

print(f"{number_associated_with_max_time} spent the longest time, {max_time} seconds, on the phone during" 
      + " September 2016.")
        



