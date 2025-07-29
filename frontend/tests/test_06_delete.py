import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_delete_users(driver):
    users_to_delete = [
        {"email": "pvsspkr@gmail.com", "password": "pru12"},
        #{"email": "pvsspkris@gmail.com", "password": "pru12"}
    ]

    for user in users_to_delete:
        driver.get("http://localhost:5173/login")
        driver.find_element(By.ID, "exampleInputEmail1").clear()
        driver.find_element(By.ID, "exampleInputEmail1").send_keys(user["email"])
        driver.find_element(By.ID, "exampleInputPassword1").clear()
        driver.find_element(By.ID, "exampleInputPassword1").send_keys(user["password"])
        driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        assert "Login successful" in alert.text
        alert.accept()

        driver.get("http://localhost:5173/home")
        driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").clear()
        driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys(user["email"])
        driver.find_element(By.XPATH, "//button[normalize-space()='Delete Account']").click()

        confirm_alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        assert "Are you sure you want to delete this account?" in confirm_alert.text
        confirm_alert.accept()

        result_alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        assert "User deleted successfully" in result_alert.text
        result_alert.accept()
