from urllib.request import build_opener, HTTPCookieProcessor, Request
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from http.cookiejar import CookieJar
from glob import glob
import urllib.request
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
import pickle
import seleniumrequests
import requests
from spynner import Browser


def ajax_complete(driver):
    try:
        return 0 == driver.execute_script("return jQuery.active")
    except WebDriverException:
        pass


def get_info(id):
    data = {'username': 'perveevm', 'password': 'vtqcjy1'}
    url = 'http://informatics.mccme.ru/login/index.php'
    #browser = webdriver.Chrome('/Users/mihail/Desktop/chromedriver')

    #browser.get(url)
    #request_cookies_browser = browser.get_cookies()
    #s = requests.Session()
    #c = [s.cookies.set(c['name'], c['value']) for c in request_cookies_browser]
    #resp = s.post(url, data)
    #dict_resp_cookies = resp.cookies.get_dict()
    #response_cookies_browser = [{'name': name, 'value': value} for name, value in dict_resp_cookies.items()]
    #c = [browser.add_cookie(c) for c in response_cookies_browser]
    #browser.get(url)
    #html = browser.page_source
    #browser.get('http://informatics.mccme.ru/submits/view.php?user_id=' + id)
    #WebDriverWait(browser, 10).until(
    #    ajax_complete, "Timeout waiting for page to load")
    #html = browser.page_source

    browser = Browser()
    browser.load('http://informatics.mccme.ru/submits/view.php?user_id=' + id)
    browser.wait_load()
    html = browser.html

    print(html)

    #browser = seleniumrequests.Chrome('/Users/mihail/Desktop/chromedriver')
    #res = browser.request('POST', url, data)
    #print(res)

    #cj = CookieJar()
    #opener = build_opener(HTTPCookieProcessor(cj))
    #req = Request(url, data.encode())
    #html = opener.open(req).read().decode()

    #print(html)


    #browser = webdriver.Chrome('/Users/mihail/Desktop/chromedriver')
    #data = {'username': 'perveevm', 'password': 'vtqcjy1'}
#
    #browser.get('http://informatics.mccme.ru/login/index.php?' + urlencode(data))
    #cookies = browser.get_cookies()
    ##req = Request('http://informatics.mccme.ru/login/index.php', data.encode())
    ##html = opener.open(req).read().decode()
#
    #html = browser.page_source#
#
    #for i in cookies:
    #    browser.add_cookie(i)
#
    #url = 'http://informatics.mccme.ru/submits/view.php?user_id=' + id
    #browser.get(url)
    #html = browser.page_source
#
    #print(html)
#
    ##cur_page = 0
#
    #while True:
    #cur_page += 1
    #html = opener.open(url).read().decode()
    #soup = BeautifulSoup(html, 'html.parser')
    #print(html)

get_info('55087')