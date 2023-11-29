import requests
from bs4 import BeautifulSoup
import csv

# URL of the webpage you want to scrape
url = "https://www.gulfjobs.com/job/civil-engineer-61378"

# Send a GET request to the webpage
response = requests.get(url)

# Parse the content of the request with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the parent 'div' with the class 'job-box'
job_box = soup.find('div', class_='job-box')

# Assuming the first <p> is Job Description, the second is Candidate Requirements, etc.
# You will need to adjust the indexing if it's different
paragraphs = job_box.find_all('p')
paragraph2 = job_box.find_all('a')

# Extract text from each <p> tag
# You may need to adjust the indexes depending on the actual structure
job_description = paragraphs[0].get_text(strip=True) if len(paragraphs) > 0 else ''
candidate_requirements = paragraphs[1].get_text(strip=True) if len(paragraphs) > 1 else ''
skills_required = paragraph2[-1].get_text(strip=True) if len(paragraph2) > 0 else ''

# Define the CSV headers
headers = ['Job Description', 'Candidate Requirements', 'Skills Required']

# Data to be written to the CSV file
rows = [
    [job_description, candidate_requirements, skills_required]
]

# Write data to CSV
with open('./output2.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(rows)

print("Data extraction complete. The CSV file has been saved.")
