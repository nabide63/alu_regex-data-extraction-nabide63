#!/usr/bin/env python3

#Here, I am importing the module required for regular expressions
import re

#Below are the example strings from which we shall extract the email addresses

example_string = "Hello ladies and gentlemen, reach us out at yu.nabide63@gu.com and kalata61@gmail.com as well as at unabo.kelo@gmail.com "

#Below is the regular expression code to extract the email addresses

expression_code = re.findall(r'\S+@\S+', example_string)    

#Below we print the output of the the expression_code, which will be the email addresses.
print(expression_code)