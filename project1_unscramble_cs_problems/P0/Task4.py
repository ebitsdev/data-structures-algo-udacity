"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

telemarketers = set()
non_telemarketers = set()
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for text_record in texts:
        # Get all the calling numbers
        non_telemarketers.add(text_record[0])
        # Get all the receiving numbers
        non_telemarketers.add(text_record[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for record in calls:
        # Get all the caller numbers        
        telemarketers.add(record[0])
        # Get all the receiving numbers
        non_telemarketers.add(record[1])
    print("These numbers could be telemarketers: ")
    # Substract the caller numbers set and the receiving numbers set to get the difference, constituting the list of possible telemarketers
    for number in sorted(telemarketers - non_telemarketers):
        print(number)

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

