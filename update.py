import httplib2
import apiclient.discovery
import timus_api
import codeforces_api
from oauth2client.service_account import ServiceAccountCredentials

SPREADSHEET_FILE = '/Users/mihail/PycharmProjects/timus_standings/spreadsheetId.cfg'
CREDENTIALS_FILE = '/Users/mihail/PycharmProjects/timus_standings/Timus results-52e7878b6481.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                               ['https://www.googleapis.com/auth/spreadsheets',
                                                                'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
with open(SPREADSHEET_FILE, 'r') as f:
    spreadsheet_id = f.read()


def get_spreadsheet(ranges):
    return service.spreadsheets().values().batchGet(
        spreadsheetId=spreadsheet_id,
        ranges=ranges
    ).execute()['valueRanges']


def update_spreadsheet(data):
    service.spreadsheets().values().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={"valueInputOption": "USER_ENTERED", "data": data}
    ).execute()


users_sheet = get_spreadsheet("'Параметры'!A1:G100")
spreadsheet = get_spreadsheet("'Результаты'!A1:G100")

users_header = users_sheet[0]['values'][0]
users = users_sheet[0]['values'][1:]

header1 = spreadsheet[0]['values'][0]
header2 = spreadsheet[0]['values'][len(users) + 2]
header3 = spreadsheet[0]['values'][len(users) + 3]

new_data = []
new_users = []

for user in users:
    timus_res, user[4] = timus_api.get_info(user[1], user[4])
    codeforces_res, user[5] = codeforces_api.get_info(user[2], user[5])
    new_data.append([user[0]] + timus_res + codeforces_res)
    new_users.append(user)

new_data.sort(key=lambda a: -int(int(a[1]) + int(a[4])))
new_data = [header1] + new_data + [[' ']] + [header2] + [header3]
new_users = [users_header] + new_users

contests = codeforces_api.get_contests()
for i in contests:
    new_data += [i]

spreadsheet[0]['values'] = new_data
users_sheet[0]['values'] = new_users

update_spreadsheet(spreadsheet)
update_spreadsheet(users_sheet)
