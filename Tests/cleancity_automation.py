from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ✅ Launch Edge browser
options = Options()
# options.add_argument("--headless")  # Optional: hide browser
driver = webdriver.Edge(options=options)
driver.get("http://localhost:8000/index.html")
driver.maximize_window()

# ========== 🔗 NAVIGATION VIA LINK TEXT ==========
def go_to_by_link(link_text, expected_page_id):
    try:
        print(f"[INFO] Clicking link '{link_text}'")
        link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, link_text))
        )
        link.click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, expected_page_id))
        )
        print(f"[PASS] Page '{expected_page_id}' is visible.\n")
        time.sleep(1)
    except Exception as e:
        driver.save_screenshot(f"error_{link_text}.png")
        print(f"[FAIL] Could not navigate via link '{link_text}':", e)
        raise

# ========== 1️⃣ LOGIN ==========
go_to_by_link("Login", "login-page")
Email = driver.find_element(By.ID, "login-email")
Email.send_keys("user@cleancity.com")
Password = driver.find_element(By.ID, "login-password")
Password.send_keys("password123")
login_btn = driver.find_element(By.XPATH, "//form[@id='login-form']//button")
login_btn.click()
login_success = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.ID, "login-success"))
)
assert login_success.is_displayed(), " Login success message not displayed"
print(" Login success message shown\n")

# ========== 2️⃣ REGISTRATION ==========
go_to_by_link("Register", "register-page")
driver.find_element(By.ID, "register-name").send_keys("Test User")
driver.find_element(By.ID, "register-email").send_keys("testuser@cleancity.com")
driver.find_element(By.ID, "register-password").send_keys("test123")
driver.find_element(By.ID, "register-confirm-password").send_keys("test123")
driver.find_element(By.XPATH, "//form[@id='register-form']//button").click()
register_success = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.ID, "register-success"))
)
assert register_success.is_displayed(), "Registration success message not shown"
print(" Registration success message shown\n")

# ========== 3️⃣ PICKUP REQUEST ==========
go_to_by_link("Home", "home-page")
driver.find_element(By.ID, "fullName").send_keys("Test Pickup")
driver.find_element(By.ID, "location").send_keys("Nairobi")
driver.find_element(By.XPATH, "//input[@value='General']").click()
driver.find_element(By.ID, "preferredDate").send_keys("2025-12-25")
driver.find_element(By.XPATH, "//form[@id='pickup-form']//button").click()
pickup_success = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.ID, "success-message"))
)
assert pickup_success.is_displayed(), "Pickup success message not displayed"
print("✅ Pickup request success message shown\n")

# ========== 4️⃣ FEEDBACK ==========
go_to_by_link("Feedback", "feedback-page")
driver.find_element(By.ID, "requestId").send_keys("REQ001")
driver.find_element(By.ID, "reason").send_keys("Missed Pickup")
driver.find_element(By.ID, "comments").send_keys("No one came on the scheduled day.")
driver.find_element(By.XPATH, "//form[@id='feedback-form']//button").click()
feedback_success = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.ID, "feedback-success"))
)
assert feedback_success.is_displayed(), " Feedback success message not shown"
print(" Feedback submitted successfully\n")

# ========== 5️⃣ ADMIN PANEL ==========
go_to_by_link("Admin", "admin-page")
request_dropdown = driver.find_element(By.ID, "requestSelect")
status_dropdown = driver.find_element(By.ID, "statusSelect")
assert request_dropdown.is_displayed() and status_dropdown.is_displayed(), " Admin dropdowns not visible"
print("Admin panel loaded with dropdowns\n")

# ✅ Done
driver.quit()
print(" All test steps completed successfully!")
