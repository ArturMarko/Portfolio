from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.kurs-selenium.pl/demo")
driver.find_element(By.XPATH, "//span[text()='Search by Hotel or City Name']").click()
driver.find_element(By.XPATH, "//div[@id='select2-drop']//input").send_keys('Dubai')
driver.find_element(By.XPATH, "//span[text()='Dubai']").click()
driver.find_element(By.NAME, "checkin").send_keys("01/10/2023")
driver.find_element(By.NAME, "checkout").send_keys("14/10/2023")
driver.find_element(By.ID, "travellersInput").click()
driver.find_element(By.ID, "adultInput").clear()
driver.find_element(By.ID, "adultInput").send_keys("4")
driver.find_element(By.ID, "childInput").clear()
driver.find_element(By.ID, "childInput").send_keys("2")
driver.find_element(By.XPATH, "//button[text()=' Search']").click()
hotels = driver.find_elements(By.XPATH, "//h4[contains(@class,'list_title')]//b")
hotel_names = [hotel.get_attribute("textContent") for hotel in hotels]
for name in hotel_names:
    print("Hotel name: " + name)
assert hotel_names[0] == 'Jumeirah Beach Hotel'
assert hotel_names[1] == 'Oasis Beach Tower'
assert hotel_names[2] == 'Rose Rayhaan Rotana'
assert hotel_names[3] == 'Hyatt Regency Perth'

driver.quit()
