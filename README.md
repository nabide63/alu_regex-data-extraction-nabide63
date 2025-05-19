# alu_regex-data-extraction-nabide63
Regex formative 

# Regex Data Extraction formative exercise

This repository contains Python scripts demonstrating how to extract structured data from text using regular expressions (`re` module). Each script focuses on extracting a different type of information, such as emails, URLs, phone numbers, credit card numbers, and currency values, from example strings in various formats.

---

## Contents

- **email_extract.py**  
  Extracts email addresses from text, supporting common email formats.

- **URL_extract.py**  
  Finds URLs starting with `http://` or `https://` in text.

- **phone_number_extract.py**  
  Extracts phone numbers in multiple formats, including:
  - (123)-456-7890
  - 234-567-8901
  - 3456789012


- **credit_card_numbers_extract.py**  
  Finds credit card numbers in formats such as:
  - 1234-5678-9012-3456
  - 1234 5678 9012 3456
  - 1234567890123456

- **currency_value_extract.py**  
  Extracts currency values with or without thousand separators,such as:
  - $19.99
  - $1,234.56
  - $2,000

---

## Usage

1. **Clone the repository**  
   ```
   git clone 
   cd into the cloned repository
   ```

2. **Running the scripts**  
   ```
   python3 
   ```
   Each script prints the extracted values to the terminal or console.

---

## Regular Expression Highlights

- **Always use raw string literals** (e.g., `r'pattern'`) for regex patterns.

---

## Example

**Extracting credit card numbers:**
```#!/usr/bin/env python3
import re

example_string = "My credit card number is 1234-5678-9012-3456 and 1234 5678 9012 3456"
credit_card_numbers = re.findall(r'\d{4}(?:[ -]?)\d{4}(?:[ -]?)\d{4}(?:[ -]?)\d{4}', example_string)
print(credit_card_numbers)
```
**Output:**
```
['1234-5678-9012-3456', '1234 5678 9012 3456']
```

---

## Notes

- Always adjust regex patterns as needed for your specific data formats.

---

**Author:**  
Yusuf Nabide  
19/05/2025

---

