"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)               
    phone_numbers = {}
    for i in range(len(calls)):
        # Check if the dictionary contains the receiver's number alreadey.
        if calls[i][1] in phone_numbers:
            # If the receiver's number exists increment the call duration time
            phone_numbers[calls[i][1]] += int(calls[i][3])
            # Check if the dictionary contains the caller's number alreadey.
            if calls[i][0] in phone_numbers:
            # If the receiver's number exists increment the call duration time
                phone_numbers[calls[i][0]] += int(calls[i][3])
            # Else add the caller's number to the dictionary
            else:
                phone_numbers[calls[i][0]] = int(calls[i][3])
        # Else add the receiver's number
        else:
            phone_numbers[calls[i][1]] = int(calls[i][3])
    # Find the key (phone number) with the longuest call duration.
    longest_call = max(phone_numbers, key=phone_numbers.get)
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(longest_call, phone_numbers[longest_call]))
        
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""