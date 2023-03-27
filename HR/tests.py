from django.test import TestCase
from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\\TestDjango\\chromedriver.exe")


def LogIn_Test(i):
    driver.get("http://127.0.0.1:8000/")
    driver.maximize_window()
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    button = driver.find_element_by_class_name("button")
    username.send_keys(key_list[i])
    password.send_keys(val_list[i])
    button.click()
    print("Test Case : "+str(i)+ " Passed")
    
my_dict = {'user1': '123', 'hello': '123', 'om': 'any', 'hr_om': 'om@999'}
key_list = list(my_dict.keys())
val_list = list(my_dict.values())
for i in range(len(my_dict)):
    LogIn_Test(i)



