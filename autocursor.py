import pyautogui
import time

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
search_query = "micheal jackson"
search_in_browser(search_query)

# Allow time for the browser to process the search
time.sleep(2)