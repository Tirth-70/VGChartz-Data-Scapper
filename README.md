# Game Data Scraper

Game Data Scraper is a Python script designed to efficiently retrieve and process game-related information from VGChartz. It uses web scraping techniques to extract data from multiple pages and provides a convenient way to store the information in a CSV file.

## Introduction

Game Data Scraper is a versatile tool for game enthusiasts, analysts, and researchers who want to gather comprehensive data about video games. It extracts information such as sales figures, publisher details, developer details, release dates, and more.

## Features

- **Concurrent Data Retrieval:** Utilizes ThreadPoolExecutor for concurrent retrieval of data from multiple pages.
- **Parallel Data Processing:** Implements ThreadPoolExecutor for parallel optimization of retrieved data.
- **Date Conversion:** Converts date formats to enhance data readability.
- **Efficient Scraping:** Utilizes BeautifulSoup for efficient web content parsing.

## Getting Started

Follow these steps to get started with Game Data Scraper.

### Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.x
- Required dependencies (NumPy, requests, BeautifulSoup, pandas)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/GameDataScraper.git
   ```
1. **Install dependencies:**

```bash
  pip install -r requirements.txt
```

### Usage

Run the script to retrieve game data from VGChartz and store it in a CSV file.

```bash
python game_data_scraper.py
```

### Functions

- **convert_date(data):** Converts date strings to datetime objects.
- **getdata(i):** Retrieves data from a specific page.
- **opti(web):** Processes web content and extracts game-related data.
### Example
```bash
# Example usage
python game_data_scraper.py
```
### Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please create an issue or submit a pull request.

### Contributors
- Shrey Patel
- Tirth Patel

### License
This project is licensed under the MIT License.

### Acknowledgments
The script uses BeautifulSoup for efficient web scraping.
Special thanks to VGChartz for providing valuable game-related data.
