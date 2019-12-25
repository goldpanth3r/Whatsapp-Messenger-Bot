from selenium import webdriver

driver = webdriver.Chrome("C:/Users/MAHE/Downloads/chromedriver_win32/chromedriver.exe")
driver.get('https://web.whatsapp.com/')

input('Enter anything after scanning QR code')

while True:

    name = input('Enter the name of user or group : ')
    msg = input('Enter your message : ')
    count = int(input('Enter the count : '))

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_13mgZ')       #class name of message box

    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_3M-N-')        #class name of send button
        button.click()

    print("Message sent!")

    rep = input("Press q to quit. Press any other key to continue: ")
    if rep == 'n':
        break