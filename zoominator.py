import time
import datetime
import subprocess
import pytz                                     # Install this with `pip install pytz`
from selenium import webdriver                  # Install this with `pip install selenium`
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
import pyautogui                                # Install this with `pip install pyautogui`


# Read Zoom credentials and invite link from file
def read_zoom_details(file_path):
    details = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Remove any leading/trailing whitespace
            if line and '=' in line:  # Ensure the line is not empty and contains '='
                key, value = line.split('=', 1)  # Split only at the first '='
                details[key.strip()] = value.strip()  # Remove extra whitespace
    return details


# Load the details
zoom_details = read_zoom_details('zoominator-details.txt')
zoom_email = zoom_details['zoom_email']
zoom_password = zoom_details['zoom_password']
invite_link = zoom_details['invite_link']
display_name = zoom_details['display_name']

def get_time_input():
    root = tk.Tk()
    root.title("Enter Start and End Time")
    root.geometry("300x250")  # Set size of the window

    tk.Label(root, text="Start Time (HH:MM):").pack(pady=5)
    start_time_entry = tk.Entry(root, width=20)
    start_time_entry.pack(pady=5)

    tk.Label(root, text="End Time (HH:MM):").pack(pady=5)
    end_time_entry = tk.Entry(root, width=20)
    end_time_entry.pack(pady=5)

    def on_submit():
        root.quit()

    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.pack(pady=10)

    root.mainloop()

    start_time = start_time_entry.get()
    end_time = end_time_entry.get()
    return start_time, end_time

def wait_until_time(target_time_str):
    timezone = pytz.timezone("US/Eastern")

    while True:
        now = datetime.datetime.now(timezone)
        current_time_str = now.strftime("%H:%M")
        
        if current_time_str >= target_time_str:
            break
        print(f"Waiting for time: {target_time_str}... Current time: {current_time_str}")
        time.sleep(15)

def setup_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver_service = Service(r'C:\Users\black\Downloads\chromedriver\chromedriver.exe')
    return webdriver.Chrome(service=driver_service, options=chrome_options)

def login_to_zoom(driver):
    driver.get("https://zoom.us/signin")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))

    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys(zoom_email)

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(zoom_password)
    password_field.send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(EC.url_contains("zoom.us"))

def join_meeting(driver):
    driver.get(invite_link)

    print("Wait to join...")
    print("Do not do anything to the browser that came up!")
    time.sleep(5)  # Wait for the page to load

    pyautogui.click(x=750, y=250)  # Click at (750, 250)

    time.sleep(2)  # Wait for the page to load after clicking

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "inputname")))
    except Exception as e:
        print(f"Element not found: {e}")
        return
    
    try:
        browser_join_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Join from your browser')]")))
        browser_join_link.click()
    except Exception as e:
        print(f"Join link not clickable: {e}")
        return

def main():
    # Get start and end times
    start_time_str, end_time_str = get_time_input()

    # Wait until the start time
    wait_until_time(start_time_str)

    # Set up the browser
    driver = setup_browser()

    # Now that the start time has been reached, continue with logging in and joining the meeting
    login_to_zoom(driver)
    join_meeting(driver)

    # Wait until the end time
    wait_until_time(end_time_str)

    # Shut down the computer (or any other desired action)
    print("End time reached. Shutting down the computer...")
    subprocess.call(["shutdown", "/s", "/t", "1"])

try:
    main()
finally:
    driver.quit()
