from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

BASE_URL = "https://the-internet.herokuapp.com"


def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


def teardown_driver(driver):
    driver.quit()


# ✅ 1. Login Success Test
def test_login_success():
    driver = setup_driver()
    try:
        driver.get(f"{BASE_URL}/login")

        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        message = driver.find_element(By.ID, "flash").text
        assert "You logged into a secure area!" in message

        print("✅ test_login_success PASSED")

    except Exception as e:
        print("❌ test_login_success FAILED:", e)

    finally:
        teardown_driver(driver)


# ❌ 2. Login Failure Test
def test_login_failure():
    driver = setup_driver()
    try:
        driver.get(f"{BASE_URL}/login")

        driver.find_element(By.ID, "username").send_keys("wrong")
        driver.find_element(By.ID, "password").send_keys("wrong")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        message = driver.find_element(By.ID, "flash").text
        assert "Your username is invalid!" in message

        print("✅ test_login_failure PASSED")

    except Exception as e:
        print("❌ test_login_failure FAILED:", e)

    finally:
        teardown_driver(driver)


# ☑️ 3. Checkbox Test
def test_checkboxes():
    driver = setup_driver()
    try:
        driver.get(f"{BASE_URL}/checkboxes")

        checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

        for checkbox in checkboxes:
            if not checkbox.is_selected():
                checkbox.click()

        assert all(cb.is_selected() for cb in checkboxes)

        print("✅ test_checkboxes PASSED")

    except Exception as e:
        print("❌ test_checkboxes FAILED:", e)

    finally:
        teardown_driver(driver)


# 🔽 4. Dropdown Test
def test_dropdown():
    driver = setup_driver()
    try:
        driver.get(f"{BASE_URL}/dropdown")

        dropdown = Select(driver.find_element(By.ID, "dropdown"))
        dropdown.select_by_visible_text("Option 2")

        selected = dropdown.first_selected_option.text
        assert selected == "Option 2"

        print("✅ test_dropdown PASSED")

    except Exception as e:
        print("❌ test_dropdown FAILED:", e)

    finally:
        teardown_driver(driver)


# ⏳ 5. Dynamic Loading Test
def test_dynamic_loading():
    driver = setup_driver()
    try:
        driver.get(f"{BASE_URL}/dynamic_loading/1")

        driver.find_element(By.CSS_SELECTOR, "#start button").click()

        wait = WebDriverWait(driver, 10)
        text = wait.until(
            EC.visibility_of_element_located((By.ID, "finish"))
        ).text

        assert "Hello World!" in text

        print("✅ test_dynamic_loading PASSED")

    except Exception as e:
        print("❌ test_dynamic_loading FAILED:", e)

    finally:
        teardown_driver(driver)


# 🚀 Test Runner
if __name__ == "__main__":
    print("\n🚀 Running Selenium Tests...\n")

    test_login_success()
    test_login_failure()
    test_checkboxes()
    test_dropdown()
    test_dynamic_loading()

    print("\n✅ All tests executed!\n")