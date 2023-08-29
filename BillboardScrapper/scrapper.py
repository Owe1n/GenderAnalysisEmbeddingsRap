# Import the necessary libraries
import requests
from bs4 import BeautifulSoup

import datetime
from dateutil.relativedelta import relativedelta

# Set the start date to 1989-03-18
start_date = datetime.date(1989, 3, 4)
end_date = start_date + relativedelta(months=12)
# Set the step size to 7 days
step = datetime.timedelta(days=7)
# Initialize the current date to the start date
current_date = start_date

while end_date < datetime.date(2022, 12, 17):

    rappers_billboard_apparition = {}

    # Loop until the current date is past the end date
    while current_date < end_date:
        # Print the current date
        print(current_date)
        response = requests.get(
            f"https://www.billboard.com/charts/rap-song/{current_date}/"
        )

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, "html.parser")

        # Use the CSS selector to find the element you want to scrape
        element = soup.select("#title-of-a-story + span")

        # Print the element's text content
        for e in element:
            if e.text.strip() not in rappers_billboard_apparition:
                rappers_billboard_apparition[e.text.strip()] = 1
            else:
                rappers_billboard_apparition[e.text.strip()] = (
                    rappers_billboard_apparition.get(e.text.strip()) + 1
                )

        # Increment the current date by the step size
        current_date += step

    sorted_rappers = sorted(
        rappers_billboard_apparition.items(), key=lambda x: x[1], reverse=True
    )

    filename = f"rappers_billboard_apparition_{start_date.year}_{end_date.year}.txt"
    f = open(f"{filename}", "w", encoding="utf-8")
    # Write the key-value pairs to the file
    for rapper in sorted_rappers:
        f.write(f"{rapper[0]}-{rapper[1]}\n")

    # Close the file
    f.close()
    start_date = end_date
    current_date = end_date
    end_date = end_date + relativedelta(months=12)

# # Download the web page from localhost
