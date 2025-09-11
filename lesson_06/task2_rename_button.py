from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/textinput")

    # Поиск и ввод текста
    driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")

    # Поиск и клик по кнопке
    driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

    # Получение текста
    button_text = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
    print("Текст кнопки:", button_text)

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    driver.quit()
