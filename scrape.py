from selenium import webdriver
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://5-ways-to-reverse-string-in-js.netlify.app/")
code = driver.find_elements_by_tag_name('code')
print(driver.title)
with open('data.js', 'w') as file:
    for idx in range(0, len(code)):
        if code[idx].text[0] != '/':
            print(code[idx].text)
            print()
            file.write(code[idx].text)
            file.write('\n\n')


time.sleep(5)
driver.quit()
