from time import sleep

from nice_modules import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# https://web.whatsapp.com/send?phone=+5492994043773&text=Mensaje%20de%20Prueba

def main():
    driver = webdriver.Firefox()
    driver.get("https://web.whatsapp.com/send?phone=+5492994043773")

    sleep(9)
    text_to_send = driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div')
    text_to_send.click()
    text_to_send.clear()
    text_to_send.send_keys("Hola, Texto de Ejemplo")
    text_to_send.send_keys(Keys.ENTER)

    sleep(5)
    driver.close()


if __name__ == '__main__':
    main()