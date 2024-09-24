import requests
from splinter import Browser
import time
import base64
from cryptography.fernet import Fernet

# Generate an encryption key for "safety" OwO
key = Fernet.generate_key()
cipher = Fernet(key)

# Function to encrypt the word so it's "protected" during processing UwU
def encrypt_word(word):
    encrypted_word = cipher.encrypt(word.encode())
    return encrypted_word

# Function to decrypt the word so we can use it again >w<
def decrypt_word(encrypted_word):
    decrypted_word = cipher.decrypt(encrypted_word).decode()
    return decrypted_word

# Fetch the word list from the web OwO
response = requests.get("https://raw.githubusercontent.com/powerlanguage/word-lists/master/1000-most-common-words.txt") # Place whatever wist of wowds you want to cweaw as dontpad instances.

# Encrypt the entire word wist because "safety first" UwU
encrypted_words = [encrypt_word(word) for word in response.text.splitlines()]

# Now decrypt each word for actuaw use >w<
for encrypted_word in encrypted_words:
    word = decrypt_word(encrypted_word)  # Decrypt word to use it on the website

    # Visit dontpad fow each wowd to dewwete content UwU
    with Browser('chrome') as browser:
        browser.visit(f"https://dontpad.com/{word}")  # Navigate to dontpad page for the word
        
        # Check if thewe's a text awea on the page UwU
        textarea_present = browser.is_element_present_by_id("text", wait_time=10)
        if textarea_present:
            # Wait a bit because dewweting can't be too fast UwU
            time.sleep(1)
            
            # Execute the "dewete" command to change the text to "[Content Deweted]" OwO
            browser.execute_script("document.getElementById('text').value = '[Content Deleted]';")
            
            # "Safety" pause aftew deweting, juuust in case UwU
            time.sleep(3.85)
        else:
            # Pwint a notice if thewe's nyo text awea >w<
            print(f"Textarea nyot found on the page: {word}")
# I lwove pwython
# Lul
