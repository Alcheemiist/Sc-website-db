import requests
from bs4 import BeautifulSoup
import os
import re

def is_valid_filename(filename):
    return not bool(re.search(r'[\\/*?:"<>|]', filename))

# List of slugs
with open('sitemap.json', 'r') as f:
    slugs = f.readlines()
i = 0
for slug in slugs:
    i += 1
    slug = slug.strip("[]").replace('"', '').replace(',', '')
    file  = slug.split('/')[-1].strip()
    print(file)
    print(i)
    # os.makedirs(file, exist_ok=True)

    url = slug
    # Fetch the page
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all elements with class 'job-box'
    for element in soup.find_all(class_='job-box'):
        # Extract the text
        text = element.get_text()
        print("read = ", text.__len__())
        # Write the text to a file
        with open(f'./gulfjob-data/{file}.txt', 'a', encoding='utf-8') as outfile:
            outfile.write(text + '\n')