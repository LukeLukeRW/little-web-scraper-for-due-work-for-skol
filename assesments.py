import selenium
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import json;import keyboard
import pyautogui

def main(i,txtsubject):
    for i in range(1,6):

        if i == 1:
            psw_input()

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        days = soup.find_all('div',class_="fc-daygrid-day-frame fc-scrollgrid-sync-inner")
        for i in days:
            try:
                txtsubject_dic = {}
                subject = i.find_all(class_="fc-event-title")

                for j in subject:
                    a = j.text.strip()
                    if a.startswith("VCE"):
                        txtsubject_dic["subject"] = a
                    else:
                        pass

                if 'subject' in txtsubject_dic: #if subject exists...
                    txtsubject_dic['date'] = (i.find('a', class_='fc-daygrid-day-number')['aria-label'])
                    txtsubject.append(txtsubject_dic)

            except ValueError:
                pass
    return txtsubject

def psw_input():
    time.sleep(1)
    pyautogui.typewrite("USERNAME GOES HERE");keyboard.press('tab');keyboard.write("password goes here :)");keyboard.press_and_release('enter')
    time.sleep(5)

def click_next_button():
    pyautogui.click(737,618)
    time.sleep(3)

def saving(txtsubject):
    with open ('Assessments.json','w') as json_file:
        json.dump(txtsubject,json_file,indent=4)


if __name__ == '__main__':

    txtsubject = []
    url = "url goes here :)"
    driver = selenium.webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(url)

    saving(main(txtsubject) )
