"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
count1 = set()
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for record in texts:
        count1.add(record[0])
        count1.add(record[1])
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    count = set()
    for record in calls:
        count1.add(record[0])
        count1.add(record[1])
    print("There are {} different telephone numbers in the records.".format(len(count1)))

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
