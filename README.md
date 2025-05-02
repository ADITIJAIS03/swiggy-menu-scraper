# Swiggy Menu Scraper 🍽️

This Python script scrapes menu items with **Buy 1 Get 1 (BOGO)** and **Veg** tags from restaurants on Swiggy. The extracted data is saved in an Excel file for further analysis. It utilizes **Selenium** for web scraping and **Pandas** for data handling.

## Overview

This project is designed to extract the food items listed on Swiggy restaurants that have special offers like "Buy 1 Get 1" and "Veg" tags. The data is collected and stored in an Excel file (`filtered_swiggy_menu.xlsx`) with restaurant details and their respective food items and prices.

### Features:
- Scrapes restaurant menu items from Swiggy.
- Filters food items that have **Buy 1 Get 1 (BOGO)** and **Veg** tags.
- Saves extracted food items, restaurant details, and special offers to an Excel file.
- Provides an easy-to-use interface for running the script and collecting data.

## Prerequisites

Before running the script, you need to have the following installed:

- **Python 3.x**: Ensure that Python 3.x is installed on your system. You can download it from [here](https://www.python.org/downloads/).
- **Chrome WebDriver**: Since the script uses Selenium with Chrome, download the correct version of [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) for your version of Google Chrome.

## Setup Instructions

1. **Clone the repository or download the files**:
    - If you have Git installed, clone the repository:
      ```bash
      git clone https://github.com/ADITIJAIS03/swiggy-menu-scraper.git
      ```
    - Or you can simply download the files as a zip and extract them.

2. **Install the required libraries**:
    Create a virtual environment (recommended), then install the dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Download ChromeDriver**:
    - Ensure that the `chromedriver.exe` is located in your system’s PATH or in the same directory as the script.
    - Download ChromeDriver [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

## How to Use

1. **Prepare the Input File**:
   - Ensure that the `filtered_swiggy_offers.xlsx` file is placed in the same directory as the script. This file should contain the restaurant names and their respective Swiggy URLs.
   
2. **Run the Script**:
    Execute the script by running:
    ```bash
    python swiggy_menu_scraper.py
    ```

3. **Script Workflow**:
    - The script will open each restaurant's link from the input Excel file (`filtered_swiggy_offers.xlsx`).
    - It will scroll through the page and scrape food items that have either the **Buy 1 Get 1** or **Veg** tag.
    - The extracted food items, their prices, and any special offers will be saved into an output Excel file: `filtered_swiggy_menu.xlsx`.

4. **Output**:
    - The script will save the extracted data into a file named `filtered_swiggy_menu.xlsx` in the same directory.
    - The Excel file will have three columns:
        - **Restaurant Name**
        - **Restaurant Link**
        - **Food Items** (with the respective price and offer like "Buy 1 Get 1")

## Example of the Output

| Restaurant Name | Restaurant Link           | Food Items                                                   |
|-----------------|---------------------------|--------------------------------------------------------------|
| ABC Restaurant  | `https://swiggy.com/abc`   | Veg Burger @ ₹150 (Buy 1 Get 1), Veg Pizza @ ₹200             |
| XYZ Kitchen     | `https://swiggy.com/xyz`   | Veg Biryani @ ₹250                                            |

## Troubleshooting

- **ChromeDriver Version Mismatch**: If you encounter issues related to the ChromeDriver version, ensure that the version of `chromedriver.exe` matches the version of Google Chrome installed on your system.
  
- **SSL Issues**: If you encounter SSL certificate verification errors, the script includes a fix using `ssl._create_default_https_context = ssl._create_unverified_context`.

## Contributing

If you find a bug or have suggestions for improvement, feel free to open an issue or make a pull request. Contributions are always welcome!

### License

This project is open-source and available under the [MIT License](LICENSE).

---

## Requirements

Ensure that the following libraries are installed:

- **Selenium**: For web scraping.
- **Pandas**: For data manipulation and saving the output to Excel.
- **OpenPyXL**: For writing to Excel files.

You can install them using the provided `requirements.txt`:

```bash
pip install -r requirements.txt
