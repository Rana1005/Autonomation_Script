from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group :')
msg = input('Enter your message : ')
input("Scan Qr code")

# //span[@title="Me"] for name of the person which you have to send the massage
# //*[@id="main"]/footer/div[1]/div[2]/div/div[2] for typing massage
# //*[@id="main"]/footer/div[1]/div[3]/button    for button press

user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()

msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
msg_box.send_keys(msg)
button = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button")
button.click()