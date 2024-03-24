import requests
from splinter import Browser
import time

response = requests.get("https://raw.githubusercontent.com/powerlanguage/word-lists/master/1000-most-common-words.txt") # Place whatever list of words you want to be cleared as dontpad instances.

words = response.text.splitlines()

for word in words:
    with Browser('chrome') as browser:
        browser.visit(f"https://dontpad.com/{word}")
        
        textarea_present = browser.is_element_present_by_id("text", wait_time=10)
        if textarea_present:

            time.sleep(1)
            
            browser.execute_script("document.getElementById('text').value = '[Content Deleted]';")
            
            time.sleep(3.85)
        else:
            print(f"Textarea not found on the page: {word}")
