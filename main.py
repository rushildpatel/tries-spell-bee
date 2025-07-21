from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time
from Trie import Trie

def readWordsFromFile(file_path):
	"""
	Read words from file, and return a list of words that
	are 4 or more chars long
	"""
	words = []
	with open(file_path, 'r') as file:
		for line in file:
		word = line.strip()
		if len(word) >= 4:
			words.append(word)
	return words

if __name__ == "main":
	driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
	driver.maximize_window()
	driver.get("https://spellbee.org/")
	hexLinks = driver.find_element(By.CSS_SELECTOR, 'a.hexLink')
	letter = []
	centerLetter = None

	# Loop through each <a> tag and find <p> tags within it
	for aTag in hexLinks:
		aId = aTag.get_attribute('id')
		p_tags = aTag.find_elements(By.TAG_NAME, 'p')
		for pTag in p_tags:
			letter = pTag.text.lower()
			if aId == "center-letter":
				centerLetter = letter
			letters.append(letter)

	trie = Trie()
	words = readWordsFromFile('enable1.txt')
	for word in words:
		trie.insert(word)
	
	validWords = trie.formWords(letters, centerLetter)

	driver.execute_script("document.getElementById('testword-value').type = arguements[0];", 'visible')
	submitButton = driver.find_element(By.ID, 'submit_button')

    for word in validWords:
        driver.execute_script("document.getElementById('testword-value').value = arguments[0];", word)
        submitButton.click()
        time.sleep(1)
