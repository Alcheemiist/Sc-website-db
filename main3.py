import re
import csv

# Sample text (you would replace this with your file's content)
with open('account.txt', 'r', encoding='utf-8') as file:
    text = file.read()

print(text.__len__())
# Keywords to search for
keywords = ["Account", "Location", "Industry", "Job Description", "Skills Required" ]

# Extract text after each keyword
def extract_info(text, keywords):
    info = {}
    for i, keyword in enumerate(keywords):
        next_keyword = keywords[i+1] if i+1 < len(keywords) else None
        if next_keyword:
            pattern = f"{keyword}:(.*?)(?=:)"
        else:
            pattern = f"{keyword}:(.*?)$"

        match = re.search(pattern, text, re.DOTALL)
        if match:
            info[keyword] = match.group(1).strip()
        else:
            info[keyword] = ""
        print(info)
    return info


# Extract information
extracted_info = extract_info(text, keywords)

# Write to CSV
with open('./output.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=keywords)
    writer.writeheader()
    writer.writerow(extracted_info)
