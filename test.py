from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#ChromeOptions options = new ChromeOptions();
#options.addArguments("user-data-dir=/path/to/your/custom/profile");

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=/path/to/your/custom/profile")
driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com/send?phone=+5492996585675")


sleep(17)
text_to_send = driver.find_element(By.XPATH, """//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]""")
text_to_send.click()
text_to_send.clear()
text_to_send.send_keys("Hola, Texto de Ejemplo")
text_to_send.send_keys(Keys.ENTER)

sleep(5)

driver.close()