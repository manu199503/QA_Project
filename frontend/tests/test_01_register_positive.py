from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_register(driver):
    driver.get("http://localhost:5173")
    driver.find_element(By.ID, "exampleInputname").send_keys("pk")
    driver.find_element(By.ID, "exampleInputEmail1").send_keys("pvsspkr@gmail.com")
    driver.find_element(By.ID, "exampleInputPassword1").send_keys("pru12")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    assert alert.text == "Registered successfully! Please Login to proceed."
    alert.accept()
