from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# load chrome driver
# URL: https://chromedriver.chromium.org/downloads

webDriverService = Service("C:/Users/Asus/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=webDriverService)

# Open whatsapp in chrome
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group = ')
message = input('Enter message = ')
count = int(input('Enter count = '))

input('press enter')

user_group = driver.find_element(By.XPATH, '//span[@title = "{}"]'.format(name))  # find user or group
user_group.click()  # open chat

message_box = driver.find_element(By.XPATH, "//div[@title='Type a message']")  # select message box

for i in range(count):
    message_box.send_keys(message)  # type the specified message
    button = driver.find_element(By.CLASS_NAME, '_1Ae7k')  # find the send button
    button.click()  # click send button
