#!/usr/bin/env python 3

#Here, I am importing the module required for regular expressions
import re

#Below are the example strings from which we shall extract the URLs

example_string = "Check out my websites at https://www.nabide63.com and https://www.kalata61.com"

#Below is the regular expression code to extract the URLs

extracted_urls = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', example_string)

#printing the extracted urls

print(extracted_urls)