from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys        
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(bot,url,phonenumber,Acpassword,MyUsername,Max):
    bot.get(url)
    wait = WebDriverWait(bot, 10)
    phone = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@autocomplete="tel-national"]')))
    phone.clear()
    phone.send_keys(phonenumber)
    time.sleep(2)
    checkMark = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="s-4 rounded-2px border-2 border-black ms-2 shrink-0"]')))
    webdriver.ActionChains(bot).move_to_element(checkMark).click(checkMark).perform()                    
    phone.send_keys(Keys.RETURN)
    time.sleep(2)
    password = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@autocomplete="current-password"]')))
    password.clear()
    password.send_keys(Acpassword)
    password.send_keys(Keys.RETURN)
    time.sleep(2)
    startUnFollow(bot,MyUsername,Max)

def startUnFollow(bot,MyUsername,Max):
    bot.get('https://virasty.com/'+MyUsername+'/followings')
    MaxUnFlollowCount = int(Max)
    UnFollowedTillNow = 0
    while True:
        try:
            # پیدا کردن همه باکس‌های کاربران با استفاده از XPath
            user_boxes = bot.find_elements(By.XPATH, '//div[contains(@class, "ms-2") and contains(@class, "grow") and contains(@class, "min-w-0")]')
            wait = WebDriverWait(bot, 10)
            if not user_boxes:
                print('هیچ باکسی یافت نشد، اسکرول کردن به پایین صفحه')
                bot.execute_script("window.scrollBy(0, 1000);")
                time.sleep(2)
                continue
            for user_box in user_boxes:
                # بررسی وجود عبارت "شما را دنبال می‌کند"
                if "شما را دنبال می‌کند" not in user_box.text:
                    try:
                        # پیدا کردن دکمه آنفالو در باکس کاربر
                        Unfollow_Button = user_box.find_element(By.XPATH, './/button[contains(@class, "n-3ocqtz") and contains(@class, "bg-transparent") and contains(@class, "border-gray-200") and contains(@class, "n-ubpna0") and contains(@class, "n-1hhqp0")]')
                        # کلیک کردن روی دکمه آنفالو
                        webdriver.ActionChains(bot).move_to_element(Unfollow_Button).click(Unfollow_Button).perform()
                        time.sleep(0.5)

                        # پیدا کردن دکمه تأیید و کلیک کردن روی آن
                        Agree_Button = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@class, "n-3ocqtz") and contains(@class, "n-ubpna0") and contains(@class, "n-a5w255") and contains(@class, "n-yqff76") and contains(@class, "h-12")]')))
                        webdriver.ActionChains(bot).move_to_element(Agree_Button).click(Agree_Button).perform()
                        
                        UnFollowedTillNow += 1
                        time.sleep(1)
                    except Exception as e:
                        print(f"خطا در پیدا کردن یا کلیک روی دکمه آنفالو: {e}")
                        continue

            # اسکرول کردن به پایین صفحه
            bot.execute_script("window.scrollBy(0, 1000);")
            time.sleep(2)  # زمان برای لود شدن عناصر جدید

        except Exception as e:
            print(f'Except caused: {e}')
            break
                        
