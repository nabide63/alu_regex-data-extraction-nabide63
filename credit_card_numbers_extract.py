#!/usr/bin/env python3

#Here, I am importing the module required for regular expressions
import re

#Below are the example strings from which we shall extract the credit card numbers in various formats

example_string = "My credit card number is 1234-5678-9012-3456 and 1234 5678 9012 3456"

#Below is the regular expression code to extract the credit card numbers    

credit_card_numbers  = re.findall(r'\d{4}(?:[ -]?)\d{4}(?:[ -]?)\d{4}(?:[ -]?)\d{4}', example_string)
print(credit_card_numbers)
