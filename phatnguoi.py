from selenium import webdriver
from selenium.webdriver.common.by import By
import time

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
element_input = driver.find_element(By.ID, input_id)
text_bien_so_xe = "92H48088"
element_input.send_keys(text_bien_so_xe)

# B5: Click vào button kiểm tra phạt nguội
input("Nhập CAPTCHA trên trình duyệt rồi nhấn Enter để tiếp tục...")  # Nhập thủ công
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

print()
