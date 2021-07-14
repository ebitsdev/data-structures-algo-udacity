"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    all_fixed_calls = []
    called_fixed_numbers = []
    called_number_codes = set()

    # Iterate through called numbers in from fixed line phone numbers in Bangalore
    for record in calls:
      # Check if the numbers calling are fixed line phone numbers
      if record[0].startswith("(080)"):
        # Get all the calls made from fixed line phone numbers in Bangalore
        all_fixed_calls.append(record[1])
        # Get only the fixed line phone numbers called by fixed line numbers in Bangalore
        if record[1].startswith("(080)"):          
          # Add the called fixed line numbers to the set of unique numbers
          called_fixed_numbers.append(record[1])
        # Add all the mobile numbers that were called by fixed phone line numbers
        if record[1].startswith("7") or record[1].startswith("8") or record[1].startswith("9"):
          called_number_codes.add(record[1][:4])
          # Add all the telemarketers numbers of the numbers called from a fixed phone number.
        elif record[1].startswith("140"):
          called_number_codes.add(record[1][:3])
          # Otherwise all the remaining fixed line numbers called from a fixed phone number.
        else:
          # Split the telephone code by the closing parentheses and manually add it
          called_number_codes.add(record[1].split(")")[0]+")")
    
    print("The numbers called by people in Bangalore have codes:")
    # Iterate over the area codes of numbers that were called from a fixed phone number in Bangalore
    for number in sorted(called_number_codes):
      print(number)
      
    # Print the percentage of calls made to other fixed line phone numbers in Bangalore from fixed lines.
    percentage_of_calls = 100*(len(called_fixed_numbers)/len(all_fixed_calls))
    print("{0:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage_of_calls))    


"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
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
