from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_register_and_login(driver):
    # Register the user first
    driver.get("http://localhost:5173/login")
    driver.find_element(By.ID, "exampleInputEmail1").send_keys("pvsspkr@gmail.com")
    driver.find_element(By.ID, "exampleInputPassword1").send_keys("pru12")
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

    # Wait for login alert and verify success
    login_alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    print(f"Login alert: {login_alert.text}")
    assert "Login successful" in login_alert.text
    login_alert.accept()
