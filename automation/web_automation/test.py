from selenium import webdriver


PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://youtube.com')



searchBox = driver.find_element_by_xpath('//*[@id="search"]')
searchBox.send_keys('The Beatles')

searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchButton.click()