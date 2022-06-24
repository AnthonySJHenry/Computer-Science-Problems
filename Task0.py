"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    print(f"First record of texts, {texts[0][0]} texts {texts[0][1]} at time {texts[0][2]}")

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    last_call = len(calls) -1 #gets last record index
    print(f"Last record of calls, {calls[last_call][0]} calls {calls[last_call][1]} at time {calls[last_call][2]}, lasting {calls[last_call][3]} seconds")



