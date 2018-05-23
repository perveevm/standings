from urllib.parse import urlencode
import urllib.request
import time
from hashlib import sha512
import random
import json
import datetime


key = '32ae792c4bc08d76b18e299becc8eef9879d7ae2'
secret = 'aaeb435e801680e306b39b64e67d610e2a6f8dec'


def genRand():
    res = ''
    for i in range(6):
        res += (random.choice('0123456789'))
    return res


def genApiSig(data, method):
    curRand = genRand()
    apiSig = curRand + '/' + method + '?'
    for i in sorted(data):
        apiSig += i + '=' + str(data[i]) + '&'
    apiSig = apiSig[:-1]
    apiSig += '#'
    apiSig += secret
    return curRand + sha512(apiSig.encode()).hexdigest()


def get_info(handle):
    data = {'apiKey': key, 'time': str(int(time.time())), 'handles': handle, 'lang': 'ru'}
    apiSig = genApiSig(data, 'user.info')
    data['apiSig'] = apiSig
    user_info = json.loads(urllib.request.urlopen('http://codeforces.com/api/user.info?' + urlencode(data)).read().decode())

    data = {'apiKey': key, 'time': str(int(time.time())), 'handle': handle, 'lang': 'ru'}
    apiSig = genApiSig(data, 'user.status')
    data['apiSig'] = apiSig
    submissions = json.loads(urllib.request.urlopen('http://codeforces.com/api/user.status?' + urlencode(data)).read().decode())

    rating = user_info['result'][0]['rating']
    tasks = list()
    today = list()
    for i in submissions['result']:
        if i['verdict'] == 'OK':
            submission_date = datetime.datetime.fromtimestamp(int(i['creationTimeSeconds']))
            cur_date = datetime.datetime.now()
            if submission_date.year == cur_date.year and submission_date.month == cur_date.month and submission_date.day == cur_date.day:
                if i['id'] not in today:
                    today.append(i['id'])
            if i['id'] not in tasks:
                tasks.append(i['id'])
    solved = len(tasks)
    solved_today = len(today)

    res = list()
    res.append(str(solved))
    res.append(str(rating))
    res.append(str(solved_today))
    return res
