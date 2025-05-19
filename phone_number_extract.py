#!/usr/bin/env python3

#Here, I am importing the module required for regular expressions
import re

#Below are the example strings from which we shall extract the phone numbers

example_string = "Call me at (123)-456-7890 or 234-567-8901 as well as at 3456789012"

#Below is the regular expression code to extract the phone numbers

phone_numbers  = re.findall(r'\+?\d{0,3}[\s.-]?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}', example_string)
print(phone_numbers)