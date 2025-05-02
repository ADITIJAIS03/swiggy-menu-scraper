import ssl
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Fix SSL issue
ssl._create_default_https_context = ssl._create_unverified_context

# Load restaurant links from Excel file
input_file = "filtered_swiggy_offers.xlsx"  # Replace with your actual file name
df_links = pd.read_excel(input_file)

def extract_filtered_swiggy_food_items(restaurant_name, url):
    options = Options()
    #options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    try:
        driver.get(url)
        time.sleep(5)  # Initial wait for JavaScript to load

        # Scroll multiple times until no more items load
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(10)  # Allow time for items to load
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break  # Stop scrolling when no new items load
            last_height = new_height

        food_items = []

        # Locate all food items
        food_elements = driver.find_elements(By.XPATH, "//div[@data-testid='normal-dish-item']")
        
        for food_element in food_elements:
            try:
                has_svg = False
                has_bogo = False

                # Check if the SVG tag (Green Checkmark) exists
                try:
                    food_element.find_element(By.XPATH, ".//div[contains(@class, 'sc-kdBSHD gtEeZP')]")
                    has_svg = True
                except:
                    pass  # Ignore if not found

                # Check if the "Buy 1 Get 1" tag exists
                try:
                    food_element.find_element(By.XPATH, ".//div[contains(@class, 'sc-aXZVg giKYGQ sc-lcIPJg irlXtI')]/span[contains(text(), 'Buy 1 Get 1')]")
                    has_bogo = True
                except:
                    pass  # Ignore if not found

                # Extract if the food item has either the SVG or BOGO tag
                if has_svg or has_bogo:
                    # Extract food name
                    food_name_element = food_element.find_element(By.XPATH, ".//div[contains(@class, 'sc-aXZVg eqSzsP')]")
                    food_name = food_name_element.text.strip() if food_name_element.text else "N/A"

                    # Extract price
                    price_element = food_element.find_element(By.XPATH, ".//div[contains(@class, 'sc-aXZVg chixpw')]")
                    price = price_element.text.strip() if price_element.text else "N/A"

                    # Label items with "Buy 1 Get 1" for clarity
                    if has_bogo:
                        food_items.append(f"{food_name} @ {price} (Buy 1 Get 1)")
                    else:
                        food_items.append(f"{food_name} @ {price}")
            except Exception as e:
                print(f"Error extracting item from {restaurant_name}: {e}")

        return "; ".join(food_items)  # Concatenate items into a single string

    except Exception as e:
        print(f"Error fetching the webpage {url}: {e}")
        return ""
    finally:
        driver.quit()

# Process each restaurant link
all_data = []
for index, row in df_links.iterrows():
    restaurant_name = row["Restaurant Name"]  # Read restaurant name
    restaurant_url = row["Link"]  # Read link from Excel
    print(f"Processing: {restaurant_name} ({restaurant_url})")
    extracted_data = extract_filtered_swiggy_food_items(restaurant_name, restaurant_url)
    all_data.append((restaurant_name, restaurant_url, extracted_data))

# Save all extracted data into an Excel file
if all_data:
    output_file = "filtered_swiggy_menu.xlsx"
    df_output = pd.DataFrame(all_data, columns=["Restaurant Name", "Restaurant Link", "Food Items"])
    df_output.to_excel(output_file, index=False)
    print(f"✅ Data successfully saved to {output_file}")
else:
    print("No matching food items found.")
