import re

# Define regular expressions pattern to match email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# Define a regular expression pattern to match credit card numbers
credit_card_pattern = r'\b(\d{4}-\d{4}-\d{4}-\d{4}|\d{16})\b'

#Function to mask sensitive data (credit card , email address)
def mask_data(match):
    return '*' * len(match.group(0))

#Open the log file for reading
with open('sample.log', 'r') as log_file:
    log_data = log_file.read()

#Mask email addresses
masked_data = re.sub(email_pattern, mask_data,log_data ) 

#Mask credit card numbers
masked_data = re.sub(credit_card_pattern, mask_data, masked_data)

#Print or save the masked log data
with open ('masked_sample_log', 'w') as masked_log_file:
    masked_log_file.write(masked_data)

print("Data masking and redaction completed. Masked log saved as 'masked_sample.log'.")
