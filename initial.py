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
history_sheet = sheet.get_worksheet(1)


try:
    #Define Current Time
    current_time = datetime.datetime.now()
    
    #Preload the spreadsheet with Labels
    sheet_instance.update('A1', 'Ethereum Calculator')
    sheet_instance.update('A2', 'Last Updated')
    sheet_instance.update('B2', str(current_time))
    sheet_instance.update('A4', 'Realtime ETH Network Stats')
    sheet_instance.update('A5', 'ETH Price USD')
    sheet_instance.update('A6', 'Network Rate')
    sheet_instance.update('A7', 'Block Time')
    sheet_instance.update('A8', 'Block Reward')
    sheet_instance.update('A9', 'Blocks 1D')
    sheet_instance.update('B9', '\=SUM(86400/B7)')
    sheet_instance.update('D4', 'Rig Stats for')
    sheet_instance.update('E4', 'rig_name')
    sheet_instance.update('D5', 'Rig Hash Rate')
    sheet_instance.update('D6', 'Rig Power Watts')
    sheet_instance.update('D7', 'Power Cost KW/H')
    sheet_instance.update('D8', 'Mining Prob')
    sheet_instance.update('E8', '\=SUM(E5/B6)')
    sheet_instance.update('D9', 'Est Blocks per Month')
    sheet_instance.update('E9', '\=SUM(E8*B9)')
    sheet_instance.update('G1', 'PSU Efficiency')
    sheet_instance.update('G2', '0.80')
    sheet_instance.update('H1', 'Pool Fee')
    sheet_instance.update('H2', '0.03')
    sheet_instance.update('G4', 'Rig Economics')
    sheet_instance.update('H5', '24H')
    sheet_instance.update('I5', '30D')
    sheet_instance.update('J5', '1Y')
    sheet_instance.update('G6', 'Revenue')
    sheet_instance.update('G7', 'Pool Fee')
    sheet_instance.update('G8', 'Cost')
    sheet_instance.update('G9', 'Profit')
    sheet_instance.update('H6' , '\=SUM((B8)*(E8*B9))*B5')
    sheet_instance.update('H7' , '\=SUM(H6*H2)')
    sheet_instance.update('H8' , '\=SUM((((E6+(E6*(1-G2)))/1000))*E7)*24')
    sheet_instance.update('H9' , '\=SUM(H6-H7-H8)')
    sheet_instance.update('I6' , '\=SUM(H6*30)')
    sheet_instance.update('I7' , '\=SUM(H7*30)')
    sheet_instance.update('I8' , '\=SUM(H8*30)')
    sheet_instance.update('I9' , '\=SUM(H9*30)')
    sheet_instance.update('J6' , '\=SUM(H6*365)')
    sheet_instance.update('J7' , '\=SUM(H7*365)')
    sheet_instance.update('J8' , '\=SUM(H8*365)')
    sheet_instance.update('J9' , '\=SUM(H9*365)')

    #Populate Initial History Table
    history_sheet.update('A1', 'current_time')
    history_sheet.update('B1', 'current_eth_usd')
    history_sheet.update('C1', 'current_eth_rate')
    history_sheet.update('D1', 'current_eth_blocktime')
    history_sheet.update('E1', 'current_eth_blockreward')
    history_sheet.update('F1', 'eth_network_block1d')
    history_sheet.update('G1', 'rig_name')
    history_sheet.update('H1', 'reported_rig_hashrate')
    history_sheet.update('I1', 'power_draw')
    history_sheet.update('J1', 'power_cost')
    history_sheet.update('K1', 'rig_prob')
    history_sheet.update('L1', 'rig_blocks_30d')
    history_sheet.update('M1', 'psu_eff')
    history_sheet.update('N1', 'pool_fee')
    history_sheet.update('O1', '24h_rev')
    history_sheet.update('P1', '24h_fee')
    history_sheet.update('Q1', '24h_cost')
    history_sheet.update('R1', '24h_profit')
    history_sheet.update('S1', '30d_rev')
    history_sheet.update('T1', '30d_fee')
    history_sheet.update('U1', '30d_cost')
    history_sheet.update('V1', '30d_profit')
    history_sheet.update('W1', '1y_rev')
    history_sheet.update('X1', '1y_fee')
    history_sheet.update('Y1', '1y_cost')
    history_sheet.update('Z1', '1y_profit')

    #Print Success Message
    print("The initial spreadsheet has been created successfully")

except:
    #Print Console Message - Error
    print("An exception occurred")