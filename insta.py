from time import sleep
from selenium import webdriver


browser = webdriver.Chrome()

for i in range(4):
    browser.get('https://www.youtube.com/watch?v=nMK94JlKRb4&list=PL2-dafEMk2A6TMJdtMZTusTbtUeWAKc3f&index='+str(i))

    sleep(5)

    browser.close()
