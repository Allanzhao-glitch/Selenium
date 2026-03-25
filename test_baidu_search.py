import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
@pytest.fixture
def browser():
    # 设置正确的驱动路径
    edge_options = Options()
    edge_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Edge(options=edge_options)
    yield driver
    driver.quit()

def test_baidu_search(browser):
    browser.get('http://localhost:8080/selenium-demo.html')
    search_box = browser.find_element(By.ID, "username-input")
    search_box.send_keys("Selenium")
    print(f"browser.title:{browser.title}")
    assert "Selenium" in browser.title