import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

# browser.get("http://suninjuly.github.io/simple_form_find_task.html")
link = "http://suninjuly.github.io/simple_form_find_task.html"
browser.get(link)

# submit_button = browser.find_element_by_id("submit_button")
submit_button = browser.find_element(By.ID, "submit_button")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()

# ждём 5 сек
time.sleep(5)

# закрываем браузер после всех манипуляций
browser.quit()

# защита от ошибок в коде и гарантированное завершение
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    time.sleep(5)
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
