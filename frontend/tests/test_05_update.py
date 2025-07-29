from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#In order to update , we need to login first , so this testcase has a pipeline to login first and then update the user details..
def test_update_user(driver):
    # Step 1: Login
    driver.get("http://localhost:5173/login")
    driver.find_element(By.ID, "exampleInputEmail1").send_keys("pvsspkr@gmail.com")
    driver.find_element(By.ID, "exampleInputPassword1").send_keys("pru12")  # replace with the correct password
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

    # Wait for login to complete via alert
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    assert alert.text == "Login successful!"
    alert.accept()

    # Step 2: Navigate to home and update info
    driver.get("http://localhost:5173/home")
    driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("pvsspkr@gmail.com")
    driver.find_element(By.XPATH, "//input[@placeholder='New name (optional)']").send_keys("Manu")
    driver.find_element(By.XPATH, "//button[normalize-space()='Update Info']").click()

    # Step 3: Confirm update success
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    assert alert.text == "Updated successfully"
    alert.accept()
