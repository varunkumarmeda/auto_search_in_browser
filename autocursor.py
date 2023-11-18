import pyautogui
import time
from faker import Faker
import random

def search_in_browser(query):
    # Open the browser (assuming it's already open)
    # Adjust the coordinates based on your screen resolution and browser position
    pyautogui.click(x=100, y=100)  # Click on the browser window

    # Focus on the search bar (you may need to adjust the coordinates)
    pyautogui.click(x=500, y=50)  # Click on the search bar

    # Type the search query
    pyautogui.typewrite(query)

    # Press enter from the keyboard key
    pyautogui.press('enter')

# Initialize Faker
fake = Faker()

# Number of searches to perform
num_searches = 30

for _ in range(num_searches):
    # Generate a random word for the search query
    random_word = fake.word()

    # Perform the search
    search_in_browser(random_word)

    # Random sleep time between 3 and 5 seconds
    sleep_time = random.uniform(3, 5)
    time.sleep(sleep_time)
