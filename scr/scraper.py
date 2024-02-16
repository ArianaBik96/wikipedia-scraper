import requests
import json
import re 
from bs4 import BeautifulSoup
"""
    A class for scraping data from the Wikipedia page of country leaders.

    This class provides methods to retrieve information about countries and their leaders
    from an external API, scrape the Wikipedia page of each leader to extract relevant data,
    and save the collected data to a JSON file.

    Attributes:
        base_url (str): The base URL of the external API.
        country_endpoint (str): The endpoint for retrieving country information.
        leaders_endpoint (str): The endpoint for retrieving leader information.
        cookies_endpoint (str): The endpoint for retrieving cookies.
        leaders_data (dict): A dictionary to store the scraped data for each country.
        cookie (dict): A dictionary containing cookies for authentication.

    Methods:
        refresh_cookie(): Refreshes the authentication cookie.
        cookie_expired(response): Checks if the cookie has expired based on the HTTP response.
        get_countries(): Retrieves a list of countries from the external API.
        get_leaders(country): Retrieves information about leaders for a given country.
        sanitize_output(text): Sanitizes text by removing unwanted patterns using regex.
        get_first_paragraph(wikipedia_url): Scrapes the first paragraph of a Wikipedia page.
        to_json_file(filepath, leaders_per_country): Saves the scraped data to a JSON file.
    """

class WikipediaScraper:
    
    def __init__(self):
        self.base_url = "https://country-leaders.onrender.com"
        self.country_endpoint = "/countries"
        self.leaders_endpoint = "/leaders"
        self.cookies_endpoint = "/cookie"
        self.leaders_data = {}
        self.cookie = self.refresh_cookie()

    def refresh_cookie(self) -> object:
        cookie_url = self.base_url + self.cookies_endpoint
        r = requests.get(cookie_url)
        cookie = r.cookies.get_dict()
        print(cookie)
        return cookie
    
    def cookie_expired(self, response) -> bool:
        if response.status_code == 401 or response.status_code == 403:
            return True
        else: 
            return False
    
    def get_countries(self) -> list:
        country_url = self.base_url + self.country_endpoint
        r = requests.get(country_url, cookies=self.cookie)
        countries = r.json()
        #print(countries, r.status_code)
        return countries
    
    def get_leaders(self, country: str) -> dict:
        leader_url = self.base_url + self.leaders_endpoint
        params = {"country": country}

        if self.cookie_expired(r):
            self.cookie = self.refresh_cookie()
            r = requests.get(leader_url, cookies=self.cookie, params=params)

        r = requests.get(leader_url, cookies=self.cookie, params=params)
        leaders = r.json()
        #print(type(leaders))
        for leader in leaders:
            wikipedia_url = leader['wikipedia_url']

            try:
                first_paragraph = self.get_first_paragraph(wikipedia_url)

            except Exception as e:
                print(f"Error fetching data for {leader['first_name']}: {e}")
                self.cookie = self.refresh_cookie()
                continue

            leader['first_paragraph'] = first_paragraph

        self.leaders_data[country] = leaders
        return self.leaders_data
    
    def sanitize_output(self, text: str):
        sanitized_text = re.sub(r'\[\d+\]', '', text)  # Remove content between square brackets []
        sanitized_text = re.sub(r'<.*?>', '', sanitized_text)  # Remove HTML tags
        sanitized_text = re.sub(r'/.*?/ ⓘ .*?;|\n', '', sanitized_text)  # Remove phonetical prononciation
        sanitized_text = re.sub(r'\([^)]*\)', '', sanitized_text)  # Remove anything after a year
        sanitized_text = re.sub(r' +', ' ', sanitized_text)  # Remove double spaces



        # Add more regex patterns as needed
        return sanitized_text
    
    def get_first_paragraph(self, wikipedia_url: str) -> str:
        req_wiki = requests.get(wikipedia_url)
        soup = BeautifulSoup(req_wiki.content, "html.parser")
        paragraphs = soup.find_all('p')
        first_paragraph = ""

        for p in paragraphs:
            if len(p) > 20:
                first_paragraph = p.text
                break
        
        sanitized_paragraph = self.sanitize_output(first_paragraph)
        return sanitized_paragraph
    
    
    @staticmethod
    def to_json_file(filepath: str, leaders_per_country: dict) -> None:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(leaders_per_country, f, ensure_ascii=False, indent=4)

        # Check if file can be read back
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(data)

    # Make a function to call this code easily
    def save(self, leaders_per_country: dict, filepath: str) -> None:
        self.to_json_file(filepath, leaders_per_country)




           
