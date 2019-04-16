import xml.etree.ElementTree as ET
import csv

from accounts_library import accounts_inuse, act_pass_acount, pass_act_acount
from accounts_transformer import acc_transformer

tree = ET.parse(input("Please enter the file here: "))
root = tree.getroot()

account_not_used = []

# name = str(input("Plese enter the name of the file: ")) + '.csv'
name = 'osv'

with open(name, 'w', encoding='utf8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Account", "Amount"])
    for data in root.findall('DATA'):
        row = []
        number_account = data.find('R020').text
        amount = float(data.find('T070').text)
        # print(amount)
        type_account = int(data.find('T020').text)
        if type_account == 1 and number_account in act_pass_acount:
            account = number_account + ' A'
            row.append(account)
            if account not in accounts_inuse and account[0] != '9':
                account_not_used.append(account)
            amount = -int(amount)  # change to float later and / 100
            row.append(amount)
        elif type_account == 1 and number_account not in act_pass_acount:
            account = number_account + ' A'
            row.append(account)
            if account not in accounts_inuse and account[0] != '9':
                account_not_used.append(account)
            row.append(amount)
        elif type_account == 2 and number_account in pass_act_acount:
            account = number_account + ' П'
            row.append(account)
            if account not in accounts_inuse and account[0] != '9':
                account_not_used.append(account)
            amount = -int(amount)
            row.append(amount)
        elif type_account == 2 and number_account not in pass_act_acount:
            account = number_account + ' П'
            row.append(account)
            if account not in accounts_inuse and account[0] != '9':
                account_not_used.append(account)
            row.append(amount)

        csv_writer.writerow(row)

if account_not_used:
    print('not used accounts in calsulations: ', account_not_used)

acc_transformer(name)
