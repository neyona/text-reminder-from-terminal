#! /usr/bin/env python3
# textReminderFromComputer.py - Python program that defines the
# textReminderFromComputer() function that texts a message to my cell from
# my computer. It is passed as a string.

# To run from terminal, run "chmod +x textReminderFromComputer.py" the first
# time it is run from the directory the program is in. Next run
# "./textReminderFromComputer.py" and fill in the input etc.

# The following is where the program is stored.
# /Users/user/Documents/Python_Projects/textReminderFromComputer.py

import os
from twilio.rest import Client

# Preset values
account_sid = '*******************************'
auth_token = '********************************'
myTwilioNumber = "+**********"  # Phone number from Twilio
myCellPhone = "+**********" # Users cell phone number

print("The program textReminderFromComputer is open")
print("Enter the message to be sent: ")
# The following takes the message you want to send.
message = input()
print("You entered " + message)

# The following sends the message.
twilioCli = Client(account_sid, auth_token)
twilioCli.messages.create(body=message, from_=myTwilioNumber, to=myCellPhone)

print("The message has been sent.")
