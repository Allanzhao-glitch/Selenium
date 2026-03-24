from selenium import webdriver

# 使用 Chrome 浏览器
# driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# 或者使用 Firefox 浏览器
# driver = webdriver.Firefox(executable_path='/path/to/geckodriver')

# 或者使用 Edge 浏览器
driver = webdriver.Edge()


#使用 get 方法打开一个网页：
driver.get('https://www.baidu.com') 


# # 强制停止页面加载
# driver.execute_script("window.stop();")

#获取页面标题
print(driver.title)

input_element = driver.find('name', 'q')
input_element.send_keys('Selenium')

# 关闭浏览器
driver.quit()
