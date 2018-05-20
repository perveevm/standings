from urllib.request import build_opener, HTTPCookieProcessor, Request
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from http.cookiejar import CookieJar
from glob import glob
import urllib.request
from bs4 import BeautifulSoup


def get_info(id):
    cj = CookieJar()
    opener = build_opener(HTTPCookieProcessor(cj))
    data = urlencode({'username': 'bottest', 'password': 'vtqcjy1'})
    req = Request('http://informatics.mccme.ru/login/index.php', data.encode())
    html = opener.open(req).read().decode()

    url = 'http://informatics.mccme.ru/submits/view.php?user_id=' + id
    cur_page = 0

    #while True:
    cur_page += 1
    html = opener.open(url).read().decode()
    soup = BeautifulSoup(html, 'html.parser')
    print(html)

get_info('55087')