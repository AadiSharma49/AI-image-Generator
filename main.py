import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils.generate_story_image import create_story_image
from dotenv import load_dotenv

load_dotenv("config/secrets.env")

def post_story(topic):
    image_path = create_story_image(topic)

    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 2
    })

    driver = webdriver.Chrome(options=chrome_options)

    # 1. Login
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)

    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    username_input.send_keys(os.getenv("INSTA_USERNAME"))
    password_input.send_keys(os.getenv("INSTA_PASSWORD"))

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    time.sleep(8)

    # 2. Close Save Login Info Popups
    try:
        not_now = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]")
        not_now.click()
        time.sleep(3)
        not_now2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]")
        not_now2.click()
        time.sleep(3)
    except:
        pass

    # 3. Go to Story Upload Page
    driver.get("https://www.instagram.com/")
    time.sleep(5)

    # You may need to implement upload via devtools script execution
    # Instagram doesn't allow story upload via web UI directly

    print(f"[INFO] Image created at {image_path}")
    print("[⚠️] Uploading stories via web is restricted. Use mobile emulation or run in Android device.")

    driver.quit()

if __name__ == "__main__":
    topic = input("Enter topic for Instagram story: ")
    post_story(topic)
