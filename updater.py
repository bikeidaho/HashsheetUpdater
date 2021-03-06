'use strict'
import config
import requests
import json
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials


#Define Google Sheets scope, creds and sheet
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('config.json', scope)
client = gspread.authorize(creds)
spreadsheetname = config.google_config['sheetname']
sheet = client.open(spreadsheetname)
sheet_instance = sheet.get_worksheet(0)


try:
    #Define Current Time
    current_time = datetime.datetime.now()
    
    #Get Bitcoin network information from Coindesk API
    coinbase_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    cb_response = requests.get(coinbase_url)
    cb_data = cb_response.json()
    current_btc_usd = cb_data["bpi"]["USD"]["rate"]
    
    #Get Ethereum network information from Etherchain API
    eth_url = 'https://etherchain.org/api/basic_stats'
    eth_response = requests.get(eth_url).json()
    eth_payload = eth_response
    current_eth_rate = eth_payload['currentStats']['hashrate']
    current_eth_blocktime = eth_payload['currentStats']['block_time']
    current_eth_blockreward = eth_payload['currentStats']['block_reward']
    current_eth_usd = eth_payload['currentStats']['price_usd']

    #HiveOS Credentials
    hive_api_url = 'https://api2.hiveos.farm/api/v2/auth/login'
    hive_username = config.hive_login['username']
    hive_password = config.hive_login['password']
    loginpayload = {"login": hive_username,  "password": hive_password}

    #Login to HiveOS and get response token
    r = requests.post(hive_api_url, data = loginpayload)
    y = json.loads(r.text)
    access_token = y['access_token']
    bearer = "Bearer "
    auth_token = bearer + access_token

    #Get HiveOS Farm Info
    url = 'https://api2.hiveos.farm/api/v2/farms'
    x = requests.get(url, data = "", headers = {"Authorization": auth_token})
    xx = json.loads(x.text)
    rig_name = xx['data'][0]['name']
    hashrates = xx['data'][0]['hashrates']
    stats = xx['data'][0]['stats']
    power_draw = stats['power_draw']
    power_cost = xx['data'][0]['power_price']
    
    #Update Google Sheet
    sheet_instance.update('B2', str(current_time))
    #sheet_instance.update('', current_btc_usd)
    sheet_instance.update('B5', current_eth_usd)
    sheet_instance.update('B6', current_eth_rate)
    sheet_instance.update('B7', current_eth_blocktime)
    sheet_instance.update('B8', current_eth_blockreward)
    sheet_instance.update('E4', rig_name)
    sheet_instance.update('E5', hashrates[0]['hashrate']*1000)
    sheet_instance.update('E6', power_draw)
    sheet_instance.update('E7', power_cost)
    
    #Print Console Message - Success
    print("Update Complete")

    
except:
    #Print Console Message - Error
    print("An exception occurred")

