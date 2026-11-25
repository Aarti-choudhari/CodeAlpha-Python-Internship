import re
from pathlib import Path

print("===== Email Address Extractor =====")

# Get the folder where this Python file is saved
folder = Path(__file__).parent

# Read emails from text file
input_file = folder / "emails.txt"

# Output file
output_file = folder / "extracted_emails.txt"

try:
    with open(input_file, "r") as file:
        text = file.read()

    # Extract email addresses
    emails = re.findall(
        r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        text
    )

    # Remove duplicate emails
    emails = list(dict.fromkeys(emails))

    # Save extracted emails
    with open(output_file, "w") as file:
        for email in emails:
            file.write(email + "\n")

    print("\nExtracted Email Addresses:")

    for email in emails:
        print(email)

    print("\nEmails saved successfully!")
    print("Total Emails Found:", len(emails))

except FileNotFoundError:
    print("Error: emails.txt file not found!")
