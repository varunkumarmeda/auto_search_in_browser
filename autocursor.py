import pyautogui
import time
import random

def search_in_browser(query):
    # Open the browser (assuming it's already open)
    # Adjust the coordinates based on your screen resolution and browser position
    pyautogui.click(x=100, y=100)  # Click on the browser window

    # Focus on the search bar (you may need to adjust the coordinates)
    pyautogui.click(x=500, y=50)  # Click on the search bar

    # Type the search query
    pyautogui.typewrite(query)

    # Press Enter to perform the search
    pyautogui.press('enter')

# Example usage
celebrities = [
    "Tom Hanks", "Jennifer Aniston", "Leonardo DiCaprio", "Beyoncé", "Brad Pitt",
    "Taylor Swift", "Dwayne Johnson", "Emma Watson", "Chris Hemsworth", "Angelina Jolie",
    "Robert Downey Jr.", "Selena Gomez", "Keanu Reeves", "Scarlett Johansson", "Will Smith",
    "Jennifer Lawrence", "Meryl Streep", "Chris Evans", "Adele", "George Clooney",
    "Shakira", "Hugh Jackman", "Natalie Portman", "Cristiano Ronaldo", "Anne Hathaway",
    "Matthew McConaughey", "Katy Perry", "Mark Wahlberg", "Johnny Depp"
]

for celebrity in celebrities:
    # Perform the search
    search_in_browser(celebrity)

    # Random sleep time between 3 and 6 seconds
    sleep_time = random.uniform(3, 6)
    time.sleep(sleep_time)