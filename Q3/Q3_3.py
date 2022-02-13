# Write your code below!

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as panda

with webdriver.Firefox() as driver:
    driver.get("www.reddit.com")
    soup = BeautifulSoup(driver.page_source)
    for tag in soup.findAll():



