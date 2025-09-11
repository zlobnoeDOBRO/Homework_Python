from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Ждем пока исчезнет спиннер загрузки
    wait = WebDriverWait(driver, 12)
    wait.until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, "#spinner"))
    )

    # Получаем третью картинкуу
    third_image = driver.find_element(
        By.CSS_SELECTOR, "#image-container img:nth-child(3)")
    print("Атрибут src третьей картинки:", third_image.get_attribute("src"))

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    driver.quit()
