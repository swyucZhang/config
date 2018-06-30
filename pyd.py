from selenium import webdriver
from PIL import ImageGrab
import os
import time


def GetBaiduUrl(obj, pagenumber):
    url = 'https://www.baidu.com/s?wd='
    page = '&pn=' + str(pagenumber * 5)
    rtn = url + obj + page
    return rtn


def GetGoogleUrl(obj, pagenumber):
    url = 'https://www.google.com/search?q='
    page = '&start=' + str(pagenumber * 5)
    rtn = url + obj + page
    return rtn


def GetBaiduResult(obj, driver, addr):
    for i in range(20):
        url = GetBaiduResult(obj, i)
        driver.get(url)
        time.sleep(2)
        im = ImageGrab.grab()
        im.save(addr, obj+str(i))
        driver.close()
        time.sleep(2)


def GetGoogleResult(obj, driver, addr):
    for i in range(20):
        url = GetGoogleResult(obj, i)
        driver.get(url)
        time.sleep(2)
        im = ImageGrab.grab()
        im.save(addr, obj+str(i))
        driver.close()
        time.sleep(2)


def main():
    # Chromedriver has to be installed
    chromedriver = '' # Path of Chromedriver
    os.environ['webdriver.chrome.driver'] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    time.sleep(2)
    driver.maximize_window()
    addr = './Image/'
    while True:
        obj = raw_input('Input what you want to search:\n')
        GetGoogleResult(obj, driver, addr)
        GetBaiduResult(obj, driver, addr)


if __name__ == '__main__':
    main()

