import requests
from bs4 import BeautifulSoup

# Function to fetch and scrape headlines from a news website
def scrape_headlines(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract headlines (specific to the website structure)
        headlines = []
        for headline in soup.find_all('h2', class_='headline'):
            headlines.append(headline.text.strip())
        
        return headlines
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

# Example usage: Scraping headlines from a news website
def main():
    url = "https://example-news-website.com"
    headlines = scrape_headlines(url)
    
    if headlines:
        print("Latest Headlines:")
        for index, headline in enumerate(headlines, start=1):
            print(f"{index}. {headline}")
    else:
        print("No headlines found or failed to fetch data.")

# Run the main function
if __name__ == "__main__":
    main()
