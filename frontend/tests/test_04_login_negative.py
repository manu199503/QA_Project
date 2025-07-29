from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_failure_invalid_password_or_user(driver):
    driver.get("http://localhost:5173/login")
    driver.find_element(By.ID, "exampleInputEmail1").send_keys("pvssp@gmail.com")  # wrong email
    driver.find_element(By.ID, "exampleInputPassword1").send_keys("pru1235475")  # wrong password
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert_text = alert.text
    print(f"Alert Text: {alert_text}")

    expected_messages = [
        "Incorrect password! Please try again.",
        "No records found"
    ]
    assert any(msg in alert_text for msg in expected_messages), f"Unexpected alert: {alert_text}"
    alert.accept()
