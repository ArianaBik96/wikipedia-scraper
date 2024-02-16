"""
Script to scrape Wikipedia for information on countries and their leaders.

Usage:
    - Import WikipediaScraper from scr.scraper module.
    - Create an instance of WikipediaScraper.
    - Use get_countries() to fetch a list of countries.
    - Use get_leaders(country) to get leaders for each country.
    - Save the data as JSON using save(data, filename).
"""

from scr.scraper import WikipediaScraper

wikiscraper = WikipediaScraper()
list_of_countries = wikiscraper.get_countries()
leaders_per_country = {}
#print(list_of_countries)
for country in list_of_countries:
    leaders_per_country[country] = wikiscraper.get_leaders(country)

new_file = "leaders.json"
wikiscraper.save(leaders_per_country, new_file)           
