import requests
from bs4 import BeautifulSoup
import os

urls = ["https://www.adeccome.com/jobs/job/a0W4I00000Ynz0RUAR",
"https://www.adeccome.com/jobs/job/a0W4I00000YnyziUAB",
"https://www.adeccome.com/jobs/job/a0W4I00000Ync12UAB",
"https://www.adeccome.com/jobs/job/a0W4I00000YnmdLUAR",
"https://www.adeccome.com/jobs/job/a0W4I00000YnaqxUAB",
"https://www.adeccome.com/jobs/job/a0W4I00000YnbxjUAB",
"https://www.adeccome.com/jobs/job/a0W4I00000Ynfy7UAB",
"https://www.adeccome.com/jobs/job/a0W4I00000YnfyvUAB",
"https://www.adeccome.com/jobs/job/a0W4I00000YnYTgUAN",
"https://www.adeccome.com/jobs/job/a0W4I00000YnbNvUAJ",
"https://www.adeccome.com/jobs/job/a0W4I00000Yii7YUAR",
"https://www.adeccome.com/jobs/job/a0W4I00000Ylua4UAB",
"https://www.adeccome.com/jobs/job/a0W4I00000Ymqc0UAB",
"https://www.adeccome.com/jobs/job/a0W4I00000Yke0sUAB",
"https://www.adeccome.com/jobs/job/a0W4I00000VsuNSUAZ",
"https://www.adeccome.com/jobs/job/a0W4I00000YmIovUAF",
"https://www.adeccome.com/jobs/job/a0W4I00000Yl8cxUAB",
"https://www.adeccome.com/jobs/job/a0W4I00000YitknUAB",
"https://www.adeccome.com/jobs/job/a0W4I00000Yl8dwUAB",
"https://www.adeccome.com/jobs/job/a0W4I00000YnYMpUAN",
"https://www.adeccome.com/jobs/job/a0W4I00000YnaqwUAB",
"https://www.adeccome.com/jobs/job/a0W4I00000YgkSzUAJ",
"https://www.adeccome.com/jobs/job/a0W4I00000YiWx8UAF",
"https://www.adeccome.com/jobs/job/a0W4I00000YnXI4UAN",
"https://www.adeccome.com/jobs/job/a0W4I00000Yjz2AUAR",
"https://www.adeccome.com/jobs/job/a0W4I00000Yk3IAUAZ",
"https://www.adeccome.com/jobs/job/a0W4I00000YhSqkUAF",
"https://www.adeccome.com/jobs/job/a0W4I00000YmugiUAB",
"https://www.adeccome.com/jobs/job/a0W4I00000YkeFdUAJ",
"https://www.adeccome.com/jobs/job/a0W4I00000YnYQIUA3",
"https://www.adeccome.com/jobs/job/a0W4I00000YnYS4UAN",
"https://www.adeccome.com/jobs/job/a0W4I00000YmEpPUAV",
"https://www.adeccome.com/jobs/job/a0W4I00000Ync1MUAR",
"https://www.adeccome.com/jobs/job/a0W4I00000YmqObUAJ",
"https://www.adeccome.com/jobs/job/a0W4I00000YmjfWUAR",
"https://www.adeccome.com/jobs/job/a0W4I00000Ync3IUAR",
"https://www.adeccome.com/jobs/job/a0W4I00000YhSqQUAV",
"https://www.adeccome.com/jobs/job/a0W4I00000YnbvaUAB",
"https://www.adeccome.com/jobs/job/a0W4I00000YQXbHUAX",
"https://www.adeccome.com/jobs/job/a0W4I00000YhOlFUAV",
"https://www.adeccome.com/jobs/job/a0W4I00000YnI5xUAF",
"https://www.adeccome.com/jobs/job/a0W4I00000YnX9mUAF",
"https://www.adeccome.com/jobs/job/a0W4I00000YjdYiUAJ",
"https://www.adeccome.com/jobs/job/a0W4I00000YihZLUAZ",
"https://www.adeccome.com/jobs/job/a0W4I00000YjXskUAF",
"https://www.adeccome.com/jobs/job/a0W4I00000YnYV8UAN",
"https://www.adeccome.com/jobs/job/a0W4I00000YhPqPUAV",
"https://www.adeccome.com/jobs/job/a0W4I00000YmqOqUAJ",
"https://www.adeccome.com/jobs/job/a0W4I00000YmqORUAZ",
"https://www.adeccome.com/jobs/job/a0W4I00000YiWykUAF"]


for url in urls:
    file  = url.split('/')[-1]
    print(file)
    # os.makedirs(file, exist_ok=True)

    # Fetch the page
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all elements with the specified class
    for element in soup.find_all(class_='job-details'):
        # Extract the text from the element
        text = element.get_text()

        # Create a filename
        filename = f'./adecco data/{file}.txt'

        # Write the text to a file
        with open(filename, 'w') as outfile:
            outfile.write(text)
