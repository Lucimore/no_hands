import datetime
import time
import sys

from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import TimeoutException

click_me = ["Сервисы для поставщиков и потребителей информации",
            "Новости",
            "Социальный калькулятор",
            "Кабинет поставщика информации",
            "Кабинет органа, назначающего меры социальной поддержки",
            "Личный кабинет гражданина",
            "Кабинет аналитика"]

file = datetime.datetime.now().strftime('%d%m_%H') + 'h_Win_10.txt'
f = open(f'{file}', mode="a", encoding="UTF-8")
f.write("\n\n<!-----InternetExplorer-----!>\n\n")


def ft_load_time(click_me):
    driver = webdriver.Ie("IEDriverServer32.exe")
    #driver = webdriver.Ie()
    #driver.get('http://egisso.ru/site/')
    driver.set_page_load_timeout(10)
    try:
        driver.get('http://google.com')
        print("You can C me")
        driver.close()
        sys.exit()
    except TimeoutException:
        print("Timeout Error")
        driver.close()
        sys.exit()
    #test_page = driver.find_element_by_link_text(click_me)
    driver.refresh()
    driver.refresh()
    driver.refresh()
    print("WTF")
    driver.close()
    sys.exit()
    try:
        test_page.click()
        # time.sleep(5)  # - не влияет на load time
        load_time = driver.execute_script(
            "return (window.performance.timing.loadEventEnd - window.performance.timing.navigationStart);")
        driver.close()
        return str(load_time)
    except UnexpectedAlertPresentException:
        driver.close()
        return "There was an ERROR"



for link in click_me:
    f.write('%-58s ' % link)
    f.write(ft_load_time(link) + "\n")

f.close()
