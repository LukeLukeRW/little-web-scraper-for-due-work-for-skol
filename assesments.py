import selenium 
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os
import json
import keyboard
from selenium.webdriver.chrome.options import Options
import pyautogui
driver = selenium.webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = "url goes here :)))))) shhhhhhhhhhhh, confidential"
driver.get(url)

txtsubject = []
one_time = True

def main(times_done):
    global one_time,txtsubject
    for k in range(times_done):

        if one_time == True:
            wait_for_psw_input()
            one_time = False

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        days = soup.find_all('div',class_="fc-daygrid-day-frame fc-scrollgrid-sync-inner")
        for i in days:
            try:
                txtsubject_dic = {}
                temp_list = []
                subject = i.find_all(class_="fc-event-title")

                for j in subject:
                    a = j.text.strip()
                    if a.startswith("VCE"):
                        txtsubject_dic["subject"] = a
                    else:
                        pass

                if 'subject' in txtsubject_dic:  # Check if subject exists
                    date1 = i.find('a', class_='fc-daygrid-day-number')
                    date = date1['aria-label']
                    txtsubject_dic['date'] = date

                    txtsubject.append(txtsubject_dic)

            except:
                print("Nuh uh")


        pyautogui.click(737,618)
        time.sleep(3)

def wait_for_psw_input():
    global one_time
    time.sleep(1)
    time.sleep(0.001);time.sleep(0.001);time.sleep(0.001);time.sleep(0.001);time.sleep(0.001);time.sleep(0.001);time.sleep(0.001);time.sleep(0.001);time.sleep(0.001);time.sleep(0.001);time.sleep(0.001);time.sleep(0.001);time.sleep(0.001);time.sleep(1);keyboard.press('l');time.sleep(.05);keyboard.press('w');time.sleep(.05);keyboard.press('a');time.sleep(.05);keyboard.press('l');time.sleep(.05);keyboard.press('0');keyboard.press('1');time.sleep(2);keyboard.press('tab');time.sleep(.5);keyboard.write("password goes here :)");keyboard.press_and_release('enter');time.sleep(0.001);time.sleep(0.001);time.sleep(0.001);time.sleep(0.001);time.sleep(0.001);time.sleep(0.001);time.sleep(0.001);time.sleep(0.001);time.sleep(0.001);time.sleep(0.001);time.sleep(0.001);time.sleep(0.001);time.sleep(0.001)
    time.sleep(5)

if __name__ == '__main__':
    main(5)
    print(txtsubject)

with open ('Assessments.json','w') as json_file:
    json.dump(txtsubject,json_file,indent=4)

'''
<div class="fc-daygrid-day-frame fc-scrollgrid-sync-inner"><div class="fc-daygrid-day-top"><a id="fc-dom-806" class="fc-daygrid-day-number" aria-label="February 21, 2024">21</a></div><div class="fc-daygrid-day-events"><div class="fc-daygrid-event-harness" style="margin-top: 0px;"><a class="fc-daygrid-event fc-daygrid-block-event fc-h-event fc-event fc-event-start fc-event-end fc-event-future source personal true" tabindex="0"><div class="fc-event-main"><span data-v-app=""><div data-v-054bf15a="" class="event-container"><b data-v-054bf15a="" class="fc-event-title">3:35pm</b> <!--v-if--> <span data-v-054bf15a="" class="fc-event-title">VCE Units 3 &amp; 4 Physics (PHY-12-E1,PHY-12-E2)<br>Summative AT 3.1: Problem solving in real world contexts (Motion in 2D)</span></div></span></div></a></div><div class="fc-daygrid-day-bottom" style="margin-top: 0px;"></div></div><div class="fc-daygrid-day-bg"></div></div>
 class="fc-event-title">3:35pm</b> <!--v-if--> <span data-v-054bf15a="" class="fc-event-title">VCE Units 3 &amp; 4 Physics (PHY-12-E1,PHY-12-E2)<br>Summative AT 3.1: Problem solving in real world contexts (Motion in 2D)</span></div></span></div></a></div><div class="fc-daygrid-day-bottom" style="margin-top: 0px;"></div></div><div class="fc-daygrid-day-bg"></div></div>

'''




