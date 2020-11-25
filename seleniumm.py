from selenium import webdriver

driver = webdriver.Chrome()
url = 'http://45.79.43.178/source_carts/wordpress/wp-login.php'
values = {'log': 'admin',
          'pwd': '123456aA'}

driver.get(url)
driver.find_element_by_name("log").send_keys('admin')
driver.find_element_by_name("pwd").send_keys('123456aA')
driver.find_element_by_id("wp-submit").click()
print(driver.find_element_by_class_name("display-name").text)

