import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from PIL import Image
import pytesseract

def run_task():
    print("Chạy chương trình kiểm tra...")
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")  # Bỏ qua lỗi SSL
    chrome_options.add_argument("--disable-web-security")  # Tắt bảo mật web
    chrome_options.add_argument("--allow-running-insecure-content")  # Cho phép nội dung không an toàn
    
    driver = webdriver.Chrome(options=chrome_options)
    try:
        # B1: Vào trang
        driver.get("https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html")

        # B2: Nhập biển kiểm soát
        name_bienkiemsat = 'BienKiemSoat'
        value_bienkiensat = "74L137860"
        element_input = driver.find_element(By.NAME, name_bienkiemsat)
        element_input.send_keys(value_bienkiensat)

        # B3: Chọn loại phương tiện
        select_element = driver.find_element(By.NAME, "LoaiXe")
        select = Select(select_element)
        select.select_by_visible_text("Xe máy")

        # B4: Xử lý Captcha
        captcha_element = driver.find_element(By.ID, "imgCaptcha")
        captcha_element.screenshot("captcha.png")

        # Nhận diện CAPTCHA
        image = Image.open("captcha.png")
        captcha_text = pytesseract.image_to_string(image).strip()
        print(f"Mã Captcha nhận diện: {captcha_text}")

        # Nhập Captcha
        captcha_input = driver.find_element(By.NAME, "txt_captcha")
        captcha_input.send_keys(captcha_text)

        # B5: Click tra cứu
        xpath_btn = '//*[@id="formBSX"]/div[2]/input[1]'
        element_btn = driver.find_element(By.XPATH, xpath_btn)
        element_btn.click()

        # Chờ kết quả
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "bodyPrint123"))
        )
        element_result = driver.find_element(By.ID, "bodyPrint123")
        text_result = element_result.text

        if 'Không tìm thấy kết quả !' in text_result:
            print("Không tìm thấy kết quả!")
        else:
            print("Tìm thấy kết quả!")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
    finally:
        driver.quit()

# Lên lịch chạy chương trình
schedule.every().day.at("06:00").do(run_task)  # Chạy lúc 6h sáng
schedule.every().day.at("17:46").do(run_task)  # Chạy lúc 12h trưa

print("Đã lên lịch chạy chương trình. Đang chờ thời gian thực hiện...")

# Vòng lặp kiểm tra lịch
while True:
    schedule.run_pending()
    time.sleep(1)  # Chờ 1 giây trước khi kiểm tra lại
