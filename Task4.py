"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

import csv
outbound_calls = set()
inbound_calls = set()
outbound_texts = set()
inbound_texts = set()

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for text in texts:
        outbound_texts.add(text[0])
        inbound_texts.add(text[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        outbound_calls.add(call[0])
        inbound_calls.add(call[1])

#subtract each set from the outbound calls set. Any remainders have not sent/received any texts and have not received any calls.
possible_telemarketers = ((outbound_calls - inbound_calls) - outbound_texts) - inbound_texts

print("These numbers could be telemarketers:\n" + str(list(possible_telemarketers)))


