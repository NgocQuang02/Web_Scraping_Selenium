from selenium import webdriver
driver = webdriver.Chrome("D:/Toa_thuoc/web_scraping/chromedriver.exe")
from selenium.webdriver.common.by import By
import time
import csv

ten =[]
gia = []
donvi = []

# #thực phẩm chức năng

url = 'https://nhathuoclongchau.com.vn/thuc-pham-chuc-nang'
driver.get(url)

while True:
    try:
        button = driver.find_element(By.XPATH, '//*[@id="category-page__products-section"]/div[2]/button')
        button.click()     
        time.sleep(2)
    except:
        elements = driver.find_elements(By.XPATH, "//h3[@class='css-tc11gt title line-clamp-3']")  
        prices = driver.find_elements(By.XPATH, "//p[@class='css-jey85n price']")
        units = driver.find_elements(By.XPATH, "//p[@class='css-pqr9s7 product_unit']")

        for element in elements:
            text = element.text
            ten.append(text) 

        for price in prices:
            text = price.text
            gia.append(text)

        for unit in units:
            text = unit.text
            donvi.append(text) 
        break


# #dược mỹ phẩm
url = 'https://nhathuoclongchau.com.vn/duoc-my-pham'
driver.get(url)
while True:
    try:
        button = driver.find_element(By.XPATH, '//*[@id="category-page__products-section"]/div[2]/button')
        button.click()     
        time.sleep(2)
    except:
        elements = driver.find_elements(By.XPATH, "//h3[@class='css-tc11gt title line-clamp-3']")  
        prices = driver.find_elements(By.XPATH, "//p[@class='css-jey85n price']")
        units = driver.find_elements(By.XPATH, "//p[@class='css-pqr9s7 product_unit']")

        for element in elements:
            text = element.text
            ten.append(text)      
            
        for price in prices:
            text = price.text
            gia.append(text)

        for unit in units:
            text = unit.text
            donvi.append(text)

        break



#chăm sóc cá nhân
url = 'https://nhathuoclongchau.com.vn/cham-soc-ca-nhan'
driver.get(url)
while True:
    try:
        button = driver.find_element(By.XPATH, '//*[@id="category-page__products-section"]/div[2]/button')
        button.click()     
        time.sleep(2)
    except:
        elements = driver.find_elements(By.XPATH, "//h3[@class='css-tc11gt title line-clamp-3']")  
        prices = driver.find_elements(By.XPATH, "//p[@class='css-jey85n price']")
        units = driver.find_elements(By.XPATH, "//p[@class='css-pqr9s7 product_unit']")

        for element in elements:
            text = element.text
            ten.append(text)    
            
        for price in prices:
            text = price.text
            gia.append(text)

        for unit in units:
            text = unit.text
            donvi.append(text)

        break

# thiet bi y te
url = 'https://nhathuoclongchau.com.vn/trang-thiet-bi-y-te'
driver.get(url)

while True:
    try:
        button = driver.find_element(By.XPATH, '//*[@id="category-page__products-section"]/div[2]/button')
        button.click()     
        time.sleep(2)
    except:
        elements = driver.find_elements(By.XPATH, "//h3[@class='css-tc11gt title line-clamp-3']")  
        prices = driver.find_elements(By.XPATH, "//p[@class='css-jey85n price']")
        units = driver.find_elements(By.XPATH, "//p[@class='css-pqr9s7 product_unit']")

        for element in elements:
            text = element.text
            ten.append(text)      
            
        for price in prices:
            text = price.text
            gia.append(text)

        for unit in units:
            text = unit.text
            donvi.append(text)
        break

with open('output.csv', 'a', newline = '', encoding = 'utf-8') as f:
    headers = ['Ten thuoc','Gia','Don vi']
    writer = csv.DictWriter(f, delimiter=',', lineterminator='\n', fieldnames=headers)
    writer.writeheader()
    for j in range(0,len(gia)):
        print(ten[j])
        print(gia[j])
        print(donvi[j])
        writer.writerow({headers[0]:ten[j],headers[1]:gia[j],headers[2]:donvi[j]})
