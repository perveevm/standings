import datetime
import urllib.request
from bs4 import BeautifulSoup


def get_month(cur_month):
    if cur_month == 'янв':
        return 1
    if cur_month == 'фев':
        return 2
    if cur_month == 'мар':
        return 3
    if cur_month == 'апр':
        return 4
    if cur_month == 'май':
        return 5
    if cur_month == 'июн':
        return 6
    if cur_month == 'июл':
        return 7
    if cur_month == 'авг':
        return 8
    if cur_month == 'сен':
        return 9
    if cur_month == 'окт':
        return 10
    if cur_month == 'ноя':
        return 11
    if cur_month == 'дек':
        return 12


def is_today(cur_date):
    day, month, year = cur_date.split()
    cur_date = datetime.datetime.now()
    cur_day, cur_month, cur_year = cur_date.day, cur_date.month, cur_date.year
    month = get_month(month)
    if int(day) == int(cur_day) and int(month) == int(cur_month) and int(year) == int(cur_year):
        return True
    else:
        return False


def get_info(judge_id):
    url = 'http://acm.timus.ru/author.aspx?id=' + judge_id + '&locale=ru'
    html = urllib.request.urlopen(url).read().decode()
    soup = BeautifulSoup(html, 'html.parser')

    res = []

    stats = soup.find('table', {'class': 'author_stats'})

    if stats is None:
        res.append('0')
        res.append('0')
        res.append('0')
        return res

    tasks = stats.contents[1].contents[1].contents[0].split()[0]
    rating = stats.contents[3].contents[1].contents[0].split()[0]
    tasks_today = 0

    url = 'http://acm.timus.ru/status.aspx?author=' + judge_id + '&status=accepted&locale=ru&count=1000'
    html = urllib.request.urlopen(url).read().decode()
    soup = BeautifulSoup(html, 'html.parser')

    submissions_even = soup.find_all('tr', {'class': 'even'})
    submissions_odd = soup.find_all('tr', {'class': 'odd'})

    submission_time = []

    for i in submissions_even:
        submission_time.append(i.contents[1].contents[2].contents[0])
    for i in submissions_odd:
        submission_time.append(i.contents[1].contents[2].contents[0])

    for i in submission_time:
        if is_today(i):
            tasks_today += 1

    res.append(tasks)
    res.append(rating)
    res.append(str(tasks_today))
    return res
