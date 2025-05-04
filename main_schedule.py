import schedule
import time
import os

def run_check():
    os.system("python check_phatnguoi.py")  # Tên file script Selenium

schedule.every().day.at("06:00").do(run_check)
schedule.every().day.at("12:00").do(run_check)

print(" Đang chạy lịch kiểm tra phạt nguội...")
while True:
    schedule.run_pending()
    time.sleep(60)
