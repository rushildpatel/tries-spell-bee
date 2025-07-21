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

