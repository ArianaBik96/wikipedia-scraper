# OpenSpace Organizer
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Description

This script is designed to scrape Wikipedia for information about countries and their leaders. It utilizes the Wikipedia API to gather data, including country names and leader details, and saves the collected information into a JSON file.

## Repo structure

```
.
├── src/
    └──scraper.py
│    
├── .gitignore
├── leaders.json
├── main.py
├── README.md
└── requirements.txt
```

## Installation

To run the script, follow these steps:

1. Clone this repository:

    ```bash
    git clone <repository-url>
    ```

2. Install the required dependencies:

    ```bash
    pip install requests beautifulsoup4
    ```

3. Run the script:

    ```bash
    python main.py
    ```


## Usage

1. Clone the repository to your local machine.

2 .To run the script, you can execute the `main.py` file from your command line:

    ```
    python main.py
    ```

3. this file:
    '''Imports the WikipediaScraper class from the `scr.scraper` module.
    '''Creates an instance of the `WikipediaScraper` class.
    '''Uses the `get_countries()` method to retrieve a list of countries.
    '''Uses the `get_leaders(country)` method to get information about leaders for a specific country.
    '''Saves the collected data to a JSON file using the `save(data, filename)` method.

## Timeline

This project took 3 days for completion.

## Personal Situation
This project was done as part of the AI Boocamp at BeCode.org. 

Connect with me on [LinkedIn](https://www.linkedin.com/in/ariana-bik-62213a107/).