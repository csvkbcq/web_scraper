import requests
from bs4 import BeautifulSoup

# Global variable to store the right_box content
right_box_html = ""

def scrape_right_box():
    url = "https://www.nseindia.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://www.google.com/'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to retrieve data: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the div with the class 'right_box'
    right_box = soup.find('div', class_='right_box')
    
    if not right_box:
        print("Could not find the 'right_box' div.")
        return
    
    global right_box_html
    # Extract only the inner HTML of the right_box div
    right_box_html = right_box.decode_contents()  # This will get the inner HTML without the div tag itself
    
    print(right_box_html)
