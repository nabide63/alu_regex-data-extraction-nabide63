#!/usr/bin/env python3

#Here, I am importing the module required for regular expressions
import re

#Below are the example strings from which we shall extract the currency values

example_string = "The price of the items ranges from $19.99 to $1,234.56 but cannot exceed $2,000"

#Below is the regular expression code to extract the currency values

currency_values  = re.findall(r'\$\d{1,3}(?:,\d{3})*(?:\.\d+)?', example_string)
print(currency_values)