import time
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

options = webdriver.FirefoxOptions()
# options.add_argument('-headless')  # headless mode
driver = webdriver.Firefox(executable_path=r'<存放 Firefox driver 的路徑>', options=options)
driver.get(r'<你想爬的網頁>')

js = "document.getElementById('u_0_c').remove();"

# 現在好像都不用
''' # 沒登入的「稍後再說」
ele = WebDriverWait(driver, 10).until(
    ec.visibility_of_element_located((By.ID, 'expanding_cta_close_button'))
)
ele.click()

# 打開留言
ele = driver.find_element_by_css_selector('._3hg-._42ft')
ele.click()'''

while True:
    try:
        # 不要有正在跑的小圈圈
        WebDriverWait(driver, 8).until_not(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '.mls.img._55ym._55yn._55yo')))
        # 找「顯示先前留言」
        # 原為 UFIPagerLink
        ele = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, '._4sxc._42ft')))  
        ele.click()
    except ElementClickInterceptedException:
        print('remove')
        # 移除下面的橫幕
        driver.execute_script(js)
    except TimeoutException:
        print('ok 1')
        break

# 按「查看更多」
for ele in driver.find_elements(By.CSS_SELECTOR, '._5v47.fss'):
    try:
        ele.click()
    # 有時候會在這邊被觸發
    except ElementClickInterceptedException:
        print('remove')
        driver.execute_script(js)

print('ok 2\n')

# 從回覆中找「你好」
gex = re.compile(r'你好')
count = 0
# 原本是 UFICommentBody
for comment in driver.find_elements_by_css_selector('span._3l3x'):
    tmp = len(gex.findall(comment.text))
    print(f'+{tmp}', end='  ')
    count += tmp
print('\nfinish.\n')
print(f'共 {count} 個「你好」')

# 等一下再關
time.sleep(5)
driver.quit()
