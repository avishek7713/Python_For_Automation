import requests
from bs4 import BeautifulSoup
from time import sleep


# Define headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

for page_number in range(1,3):

    # url with dynamic page number
    url = "https://www.goodreads.com/list/show/205255.Goodreads_Editors_Book_Picks_for_2024?page=" +str(page_number)

    # try and except block to handle any error
    try:
        # sending get requests including the headers
        response = requests.get(url, headers= headers)

        # html parser
        soup = BeautifulSoup(response.content, 'html.parser')

        # find the span tag with respective attributes
        span_tag_title = soup.find_all("span", {"itemprop": "name", "role": "heading"})

        # initializing a list to hold all the titles
        titles = []

        #extract and print the titles extracted from the span tags     
        for span in span_tag_title:

            # append the extracted title to the titles list
            titles.append(span.text.strip())

        # find the span tag for author with respective attributes
        span_tag_author = soup.find_all("span", {"itemprop": "author"})

        # initializing the authors list to hold all the extracted authors
        authors = []

        #iterating through the extracted author span tags to extract the texts
        for span in span_tag_author:
            authors.append(span.text.strip())
        
        # merging the two lists holding titles and authors as a dictionery
        books_with_authors = dict(zip(titles, authors))

        # printing all the keys and values of the dictionery as text
        for key, value in books_with_authors.items():
            print(f"{key}:  {value}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}") 

    sleep(5)