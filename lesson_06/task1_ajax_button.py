from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/ajax")
    driver.find_element(By.ID, "ajaxButton").click()

    message = WebDriverWait(driver, 16).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
    )
    print("Текст из зеленой плашки:", message.text)

except Exception as e:
    print(f"Произошла ошибка: {e}")

    driver.quit()
