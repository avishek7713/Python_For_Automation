import requests
from bs4 import BeautifulSoup

# URL of the Goodreads page
url = "https://www.goodreads.com/genres/new_releases/fiction"

# Define headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    # Send GET request with headers
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise error for HTTP codes >= 400
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find and extract alt attributes
    book_images = soup.find_all('img', class_='bookImage')
    for img in book_images:
        alt_text = img.get('alt', 'No alt text found')  # Safely get alt attribute
        print(alt_text)
except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
