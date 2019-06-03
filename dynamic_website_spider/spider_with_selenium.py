from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('http://127.0.0.1:5000')

student_li_list = driver.find_elements_by_css_selector('li')

students = []
for student_li in student_li_list:
  students.append(student_li.text.strip())

print('=================================')
print(students)

driver.close()