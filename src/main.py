import json
import re

# 1. Open and read the messy text file
with open("input/raw-text.txt", "r") as file:
    raw_text = file.read()

# 2. regex patterns
phone_pattern = r"\+?250[\s\-]?7\d{2}[\s\-]?\d{3}[\s\-]?\d{3}"
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
card_pattern = r"\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}"
html_pattern = r"<[^>]+>"

# 3. Matching the patterns
all_phones = re.findall(phone_pattern, raw_text)
all_emails = re.findall(email_pattern, raw_text)
all_cards = re.findall(card_pattern, raw_text)
all_html_tags = re.findall(html_pattern, raw_text)

# 4. Sort ALU emails
official_emails = []
alumni_emails = []
si_emails = []

for email in all_emails:
    if email.endswith("@alueducation.com"):
        official_emails.append(email)
    elif email.endswith("@alumni.alueducation.com"):
        alumni_emails.append(email)
    elif email.endswith("@si.alueducation.com"):
        si_emails.append(email)

# 5. Protecting credit card numbers by masking all but the last 4 digits
safe_cards = []
for card in all_cards:

    masked = "****-****-****-" + card[-4:]
    safe_cards.append(masked)

# 6. Checking if the file contains any bad HTML tags
if len(all_html_tags) > 0:
    security_message = "Warning: Unsafe HTML tags found!"
else:
    security_message = "Clear: No unsafe tags found."

# 7. Dictionary for the data
output_data = {
    "security_status": security_message,
    "phone_numbers": all_phones,
    "masked_credit_cards": safe_cards,
    "alu_emails": {
        "official": official_emails,
        "alumni": alumni_emails,
        "scholar_system": si_emails,
    },
}

# 8. Saving the data
with open("output/sample-output.json", "w") as out_file:
    json.dump(output_data, out_file, indent=4)

print("Data extraction and processing complete. Output saved to output/sample-output.json")
