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


users = get_spreadsheet("'Параметры'!A1:D100")[0]['values'][1:]
spreadsheet = get_spreadsheet("'Результаты'!A1:D100")
header = spreadsheet[0]['values'][0]
new_data = []

for user in users:
    new_data.append([user[0]] + timus_api.get_info(user[1]) + codeforces_api.get_info(user[1]))

new_data.sort(key=lambda a: -int(a[1]))
new_data = [header] + new_data
spreadsheet[0]['values'] = new_data

update_spreadsheet(spreadsheet)
