from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import pytesseract
import time
import io
import base64


# Khởi tạo trình duyệt dùng Chrome
driver = webdriver.Chrome()
driver.get("https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.htm")
print(driver.title)
#driver.quit()
#print()

# B3: (Không cần chọn Option Xe máy - trang thật không có)
#input_selector = "#mdsSubmit > label:nth-child(4) > input[type=radio]"
#element_xe_may = driver.find_element(By.CSS_SELECTOR, input_selector)
#element_xe_may.click()

# B4: Điền biển số xe máy vào ô tìm kiếm
input_id = "checkPlate"
try:
    element_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, input_id))
    )
    text_bien_so_xe = "92H48088"
    element_input.send_keys(text_bien_so_xe)
except:
    print("Không tìm thấy ô nhập biển số xe.")
    driver.quit()
    exit()



# === B3: Trích xuất CAPTCHA bằng pytesseract ===
# === B3: Trích xuất CAPTCHA bằng pytesseract (đã cải tiến) ===
time.sleep(20)  # đợi ảnh CAPTCHA tải xong

captcha_img = driver.find_element(By.ID, "captchaimg")
captcha_src = captcha_img.get_attribute("src")

# Nếu CAPTCHA ở dạng base64
if "data:image" in captcha_src:
    image_base64 = captcha_src.split(',')[1]
    image_data = base64.b64decode(image_base64)
    image = Image.open(io.BytesIO(image_data))

    # Xử lý ảnh để OCR tốt hơn
    image = image.convert("L")  # chuyển sang grayscale
    image = image.point(lambda x: 0 if x < 140 else 255)  # nhị phân hóa đơn giản
    #image.save("captcha.png")  # lưu ra file nếu muốn kiểm tra

    # OCR trích xuất mã captcha
    captcha_text = pytesseract.image_to_string(image, config='--psm 8').strip()
    print("CAPTCHA nhận dạng:", captcha_text)
else:
    print("CAPTCHA không ở định dạng base64, cần xử lý khác (tải file).")
    driver.quit()
    exit()


# B4: Nhập CAPTCHA vào input
captcha_input = driver.find_element(By.ID, "captcha")
captcha_input.send_keys(captcha_text)


# B5: Click vào button kiểm tra phạt nguội
#input("Nhập CAPTCHA trên trình duyệt rồi nhấn Enter để tiếp tục...")  # Nhập thủ công
xpath_btn = "//*[@id='btnTraCuu']"
element_btn = driver.find_element(By.XPATH, xpath_btn)
element_btn.click()

# B6: Kiểm tra kết quả hiển thị phạt nguội
time.sleep(5)  # Đợi trang load kết quả
result_id = "ketqua"
result_element = driver.find_element(By.ID, result_id)
text_result = result_element.text

if "không tìm thấy" in text_result.lower():
    print("Không có vi phạm")
else:
    print("Có vi phạm")

print("Giữ trình duyệt mở trong 5 phút...")
time.sleep(300)

# Đóng trình duyệt (nếu muốn)
driver.quit()