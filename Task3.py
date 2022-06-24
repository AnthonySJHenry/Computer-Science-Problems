"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    
area_codes = set()
calls_from_Bangalore = 0
calls_to_Bangalore = 0 #calls to Bangalore from within Bangalore
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
          if call[0][:5] == "(080)":
                calls_from_Bangalore += 1
                #enclosed in brackets
                if call[1][0] == "(":
                      stop_index = call[1].find(")") + 1
                      area_codes.add(call[1][:stop_index])
                      
                #starts w/ 7, 8, or 9 and four digits long
                if call[1][0] == "7" or call[1][0] == "8" or call[1][0] == "9":
                      area_codes.add(call[1][:4])
                      
                #no brackets, starts with 140
                if call[1][:3] == "140":
                      area_codes.add(call[1][:3])
                
                if call[1][:5] == "(080)":
                      calls_to_Bangalore += 1

percent_of_calls_within_Bangalore = round((calls_to_Bangalore/calls_from_Bangalore)*100, 2) #percent of calls from land lines in Bangalore to other land lines in Bangalore
print("The numbers called by people in Bangalore have codes:\n" + str(list(sorted(area_codes))))
print(f"{percent_of_calls_within_Bangalore} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

                
                

