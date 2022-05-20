from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pynput
from pynput.keyboard import Key, Controller
import gspread

## LOGIN INFO
nLogin = 'REDACTED'
nID = '115197169'

cLogin = 'REDACTED'
cID = '115197169'

jLogin = 'REDACTED'
jID = 'REDACTED'

## INITIALIZE
driver = webdriver.Chrome(ChromeDriverManager().install())
keyboard = Controller()
gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('REDACTED')

for i in range(3):
    if i == 0:
        useSheet = sh.get_worksheet(0)
        useLogin = nLogin
        useID = nID
    elif i == 1:
        useSheet = sh.get_worksheet(1)
        useLogin = cLogin
        useID = cID
    else:
        useSheet = sh.get_worksheet(2)
        useLogin = jLogin
        useID = jID
    if useSheet.cell(3, 3).value == "No":
        ## OPEN LOGIN
        driver.get('https://www.imleagues.com/spa/account/ssoredirect?schoolId=4395e0c781af4905a4088a9561509399')
        time.sleep(20)

        ## ENTER LOGIN INFO
        keyboard.type(useLogin)
        time.sleep(10)

        ## CANCEL PUSH
        keyboard.type('\t\t\t\t\t\t\t\t\t')
        time.sleep(1)
        keyboard.type(' ')
        time.sleep(1)
        keyboard.type('\t')
        time.sleep(1)
        keyboard.type(' ')
        time.sleep(3)
                   
        ## ENTER MFA CODE
        iframe = driver.find_element_by_xpath("//iframe[@id='duo_iframe']")
        driver.switch_to.frame(iframe)
        elem = driver.find_element_by_xpath('//*[@id="passcode"]')
        elem.click()
        keyboard.type(useSheet.cell(3,5).value + '\n')
        time.sleep(5)

        ## GO TO SIGNUP PAGE
        driver.get(useSheet.cell(3,4).value)
        time.sleep(5)

        ## CLICK SIGNUP
        elem = driver.find_element_by_class_name('iml-fitness-event-btn')
        elem.click()
        time.sleep(7)

        ## ENTER UID
        elem = driver.find_element_by_name('txtSID')
        elem.click()
        keyboard.type(useID)

        ## CLICK SIGN UP
        elem = driver.find_element_by_xpath('//button[contains(text(), "Sign Up")]')
        elem.click()

        ## CLOSE
        driver.close()
        
driver.quit()

