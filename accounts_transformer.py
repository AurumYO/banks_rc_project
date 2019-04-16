import xml.etree.ElementTree as ET
import csv

import bal_pnl_lines as bp
from financial_statements import di


def acc_transformer(name):
    for data in csv.DictReader(open(name), delimiter=','):
    # cash with NBU
        if str(data['Account']) in bp.cash:
            di['Cash'] += float(data['Amount'])
        if str(data['Account']) in bp.BM:
            di["BM"] += float(data['Amount'])
        if str(data['Account']) in bp.NBU_unt_call:
            di["NBU until call"] += float(data['Amount'])
        if str(data['Account']) in bp.NBU_due:
            di["NBU due"] += float(data['Amount'])
        if str(data['Account']) in bp.FOP:
            di["FOP"] += float(data['Amount'])
        # Value Papers NBU
        if str(data['Account']) in bp.trade_VP_NBU:
            di["Trade VP NBU"] += float(data['Amount'])
            print(di["Trade VP NBU"], 'di["Trade VP NBU"]')
        if str(data['Account']) in bp.forsale_VP_NBU:
            di["For sale VP NBU"] += float(data['Amount'])
        if str(data['Account']) in bp.due_rep_VP_NBU:
            di["Due to payment VP NBU"] += float(data['Amount'])
        if str(data['Account']) in bp.issue_NBU:
            di["Issue NBU"] += float(data['Amount'])
        if str(data['Account']) in bp.provis_VP_NBU:
            di["Provisions VP NBU"] += float(data['Amount'])
        # Interbank
        if str(data['Account']) in bp.till_call:
            di["Until request"] += float(data['Amount'])
        if str(data['Account']) in bp.overn_VP:
            di["Overnight"] += float(data['Amount'])
        if str(data['Account']) in bp.st_interbank:
            di["S/T interbank"] += float(data['Amount'])
        if str(data['Account']) in bp.lt_interbank:
            di["L/T interbank"] += float(data['Amount'])
        if str(data['Account']) in bp.overdue_interbank:
            di["Overdue interbank"] += float(data['Amount'])
        if str(data['Account']) in bp.provis_interbank:
            di["Provisions interbank"] += float(data['Amount'])
        # Trade portfolio - Value papers by fair value
        if str(data['Account']) in bp.trade_port:
            di["Trade portfolio (FV)"] += float(data['Amount'])
        # Portfolio fo sale
        if str(data['Account']) in bp.port_brutto_fs:
            di["Portfolio-brutto"] += float(data['Amount'])
        if str(data['Account']) in bp.provis_fs:
            di["Provisions (Portfolio for sale)"] += float(data['Amount'])
        # Loans legal entities
        if str(data['Account']) in bp.bill_fact_repo_leloans:
            di["bills factoring repo (loans to l/e)"] += float(data['Amount'])
        if str(data['Account']) in bp.corp_purpos_leloans:
            di["corporate purposes (loans to l/e)"] += float(data['Amount'])
        if str(data['Account']) in bp.investment_leloans:
            di["investment loans (loans to l/e)"] += float(data['Amount'])
        if str(data['Account']) in bp.mortgage_leloans:
            di["mortgage loans to l/e"] += float(data['Amount'])
        if str(data['Account']) in bp.overdraft_leloans:
            di["overdrafts to l/e"] += float(data['Amount'])
        if str(data['Account']) in bp.municipality_leloans:
            di["municipality loans"] += float(data['Amount'])
        if str(data['Account']) in bp.overdue_deeval_leloans:
            di["overdue/devaluated loans to l/e"] += float(data['Amount'])
        # Loans private individuals
        if str(data['Account']) in bp.consumer_loans:
            di["consumer loans PI"] += float(data['Amount'])
        if str(data['Account']) in bp.mortgage_piloans:
            di["mortgage PI"] += float(data['Amount'])
        if str(data['Account']) in bp.overdraft_piloans:
            di["overdraft PI"] += float(data['Amount'])
        if str(data['Account']) in bp.investment_piloans:
            di["to investments activity"] += float(data['Amount'])
        if str(data['Account']) in bp.overdue_deeval_piloans:
            di["overdue/devaluated PI"] += float(data['Amount'])
        if str(data['Account']) in bp.provisions_piloans:
            di["provisions PI loans"] += float(data['Amount'])
        # Valued papaers due to repayment
        if str(data['Account']) in bp.port_brutto_vp:
            di["portfolio brutto VP"] += float(data['Amount'])
        if str(data['Account']) in bp.provisions_vp:
            di["provisions VP"] += float(data['Amount'])
        # Investments in SC and Associates
        if str(data['Account']) in bp.investment_sc_associates:
            di["Investments to sub and associates"] += float(data['Amount'])
        # Main assets
        if str(data['Account']) in bp.main_assets:
            di["Main assets"] += float(data['Amount'])
        # Intangibles
        if str(data['Account']) in bp.intagibl:
            di["Intangibles"] += float(data['Amount'])
        # accrued income
        if str(data['Account']) in bp.mbk_ai:
            di["MBK AI"] += float(data['Amount'])
        if str(data['Account']) in bp.vp_ai:
            di["VP AI"] += float(data['Amount'])
        if str(data['Account']) in bp.le_ai:
            di["LE AI"] += float(data['Amount'])
        if str(data['Account']) in bp.pi_ai:
            di["PI AI"] += float(data['Amount'])
        if str(data['Account']) in bp.overdue_income_ai:
            di["overdue income AI"] += float(data['Amount'])
        if str(data['Account']) in bp.overdue_income_ai2:
            di["overdue income2 AI"] += float(data['Amount'])
        if str(data['Account']) in bp.provisions_ai:
            di["provisions AI"] += float(data['Amount'])
        # deffered tax
        if str(data['Account']) in bp.deferred_tax:
            di["Deferred tax"] += float(data['Amount'])
        # other assets
        if str(data['Account']) in bp.account_payables:
            di["account payables"] += float(data['Amount'])
        if str(data['Account']) in bp.other_assets:
            di["other assets"] += float(data['Amount'])
        if str(data['Account']) in bp.provisions_oa:
            di["provisions other assets"] += float(data['Amount'])
        # long term assets for sale
        if str(data['Account']) in bp.lt_assets_for_sale:
            di["LT asset for sale"] += float(data['Amount'])
        # LIABILITIES section
        # Interbank until call
        if str(data['Account']) in bp.until_call_interbank:
            di["until call interbank"] += float(data['Amount'])
        if str(data['Account']) in bp.overnight_interbank:
            di["overnight interbank"] += float(data['Amount'])
        if str(data['Account']) in bp.shortterm_liab_interbank:
            di["short term lbl interbank"] += float(data['Amount'])
        if str(data['Account']) in bp.longterm_liab_interbank:
            di["long term lbl interbank"] += float(data['Amount'])
        if str(data['Account']) in bp.overdue_liab_interbank:
            di["overdue liability interbank"] += float(data['Amount'])
        # funds of legal entities
        if str(data['Account']) in bp.due_funds_le:
            di["due funds of LE"] += float(data['Amount'])
        if str(data['Account']) in bp.due_statesect_le:
            di["due funds state sector LE"] += float(data['Amount'])
        if str(data['Account']) in bp.untillcall_funds_le:
            di["until call funds LE"] += float(data['Amount'])
        if str(data['Account']) in bp.untilcall_statesect_le:
            di["until call funds state sector LE"] += float(data['Amount'])
        if str(data['Account']) in bp.untilcall_polpatry_le:
            di["until political parties LE"] += float(data['Amount'])
    # funds private individuals
        if str(data['Account']) in bp.due_funds_pi:
            di["due funds PI"] += float(data['Amount'])
        if str(data['Account']) in bp.untcall_funds_pi:
            di["until call funds PI"] += float(data['Amount'])
    # savings certificates
        if str(data['Account']) in bp.saving_certif:
            di["Savings certificates"] += float(data['Amount'])
    # debt VP
        if str(data['Account']) in bp.debt_vp:
            di["Debt value papers"] += float(data['Amount'])
    # accrued expenses
        if str(data['Account']) in bp.mbk_ae:
            di["MBK accrued exp"] += float(data['Amount'])
        if str(data['Account']) in bp.clients_ae:
            di["clients accrued exp"] += float(data['Amount'])
        if str(data['Account']) in bp.vp_ae:
            di["VP accrued exp"] += float(data['Amount'])
        if str(data['Account']) in bp.others_ae:
            di["others accrued expenses"] += float(data['Amount'])
    # deferred tax liability
        if str(data['Account']) in bp.deferred_tax_liabl:
            di["Deferred tax liability"] += float(data['Amount'])
    # Other liabilities
        if str(data['Account']) in bp.unregist_chart:
            di["unregistered charter"] += float(data['Amount'])
        if str(data['Account']) in bp.dividends:
            di["dividends"] += float(data['Amount'])
        if str(data['Account']) in bp.other_other_liabl:
            di["others other liabilities"] += float(data['Amount'])
    # subordinated debt
        if str(data['Account']) in bp.subord_debt:
            di["Subordinated debt"] += float(data['Amount'])
    # charter and equity
        if str(data['Account']) in bp.charter:
            di["Charter"] += float(data['Amount'])
        if str(data['Account']) in bp.own_shares:
            di["Own shares"] += float(data['Amount'])
        if str(data['Account']) in bp.emission_diff:
            di["emission differences"] += float(data['Amount'])
        if str(data['Account']) in bp.prov_capdivid_funds:
            di["reserves cap divid and funds"] += float(data['Amount'])
    # provisions reevalutioans
        if str(data['Account']) in bp.realest_reeval:
            di["real estate reeval"] += float(data['Amount'])
        if str(data['Account']) in bp.intangibl_reeval:
            di["intangibles reeval"] += float(data['Amount'])
        if str(data['Account']) in bp.vp_reeval:
            di["VP reevaluation"] += float(data['Amount'])
    # Last year result
        if str(data['Account']) in bp.ly_result:
            di["Last year result"] += float(data['Amount'])
    # PNL starts here
    # Net income
        if str(data['Account']) in bp.net_perc_income:
            di["% MBK income"] += float(data['Amount'])
        if str(data['Account']) in bp.net_le_income:
            di["% income LE"] += float(data['Amount'])
        if str(data['Account']) in bp.net_pi_income:
            di["% income PI"] += float(data['Amount'])
        if str(data['Account']) in bp.net_other_income:
            di["% income others"] += float(data['Amount'])
    # Net expenses
        if str(data['Account']) in bp.mbk_net_exp:
            di["% MBK expenses"] += float(data['Amount'])
        if str(data['Account']) in bp.le_net_exp:
            di["% LE expenses"] += float(data['Amount'])
        if str(data['Account']) in bp.pi_net_exp:
            di["% PI expenses"] += float(data['Amount'])
        if str(data['Account']) in bp.other_net_exp:
            di["% other expenses"] += float(data['Amount'])
    # net commission income
        if str(data['Account']) in bp.commiss_income:
            di["commission income"] += float(data['Amount'])
        if str(data['Account']) in bp.commiss_expenses:
            di["commission expenses"] += float(data['Amount'])
    # trade income
        if str(data['Account']) in bp.vp_income:
            di["VP_income"] += float(data['Amount'])
        if str(data['Account']) in bp.curren_bm_income:
            di["currency and BM income"] += float(data['Amount'])
    # dividends income
        if str(data['Account']) in bp.dividends_income:
            di["Dividends income"] += float(data['Amount'])
    # Capital income
        if str(data['Account']) in bp.capital_income:
            di["Capital income"] += float(data['Amount'])
    # Other incomes
        if str(data['Account']) in bp.other_incomes:
            di["Other incomes"] += float(data['Amount'])
    # Administrative expenses
        if str(data['Account']) in bp.admin_expenses:
            di["Administrative expenses"] += float(data['Amount'])
    # Personnel expenses
        if str(data['Account']) in bp.personel_expenses:
            di["Personnel expenses"] += float(data['Amount'])
    # Losses on capital participation
        if str(data['Account']) in bp.loss_on_capital:
            di["Losses on shares in capital"] += float(data['Amount'])
    # Other expenses
        if str(data['Account']) in bp.others_expenses:
            di["Others expenses"] += float(data['Amount'])
    # Net losses on provisions
        if str(data['Account']) in bp.loss_on_provision:
            di["Loss on provisions"] += float(data['Amount'])
    # Profit tax
        if str(data['Account']) in bp.profit_tax:
            di["Profit tax"] += float(data['Amount'])

        di['Cash in NBU cash and BM'] = di['Cash'] + di['BM'] + di['NBU until call'] + di['NBU due'] + di['FOP']
        di['VP NBU'] = di['Trade VP NBU'] + di['For sale VP NBU'] + di['Due to payment VP NBU'] + di['Issue NBU']\
                        + di['Provisions VP NBU']
        di['Interbank'] = di['Until request'] + di['Overnight'] + di['S/T interbank'] + di['L/T interbank']\
                          + di['Overdue interbank'] + di['Provisions interbank']
        di['Portfolio for sale'] = di['Portfolio-brutto'] + di['Provisions (Portfolio for sale)']
        di['Legal entities loans'] = di['bills factoring repo (loans to l/e)'] + di['corporate purposes (loans to l/e)'] \
                                      + di['investment loans (loans to l/e)'] + di['mortgage loans to l/e'] \
                                      + di['overdrafts to l/e'] + di['municipality loans'] \
                                      + di['overdue/devaluated loans to l/e']
        di['Private individ loans'] = di['consumer loans PI'] + di['mortgage PI'] + di['overdraft PI'] \
                                      + di['to investments activity'] + di['overdue/devaluated PI']\
                                      + di['provisions PI loans']
        di['Loans:'] = di['Legal entities loans'] + di['Private individ loans']
        di['VP due to repayment'] = di['portfolio brutto VP'] + di['provisions VP']
        di['Accrued income'] = di['MBK AI'] + di['VP AI'] + di['LE AI'] + di['PI AI'] + di['overdue income AI']\
                               + di['overdue income2 AI'] + di['provisions AI']
        di['Others assets'] = di['account payables'] + di['other assets'] + di['provisions other assets']
        di['TOTAL ASSETS'] = di['Cash in NBU cash and BM'] + di['VP NBU'] + di['Interbank'] + di['Trade portfolio (FV)']\
                             + di['Portfolio for sale'] + di['Loans:'] + di['VP due to repayment']\
                             + di['Investments to sub and associates'] + di['Main assets'] + di['Intangibles']\
                             + di['Accrued income'] + di['Deferred tax'] + di['Others assets'] + di['LT asset for sale']

        # Accumulative liabilities
        di['Interbank obl'] = di['until call interbank'] + di['overnight interbank']+ di['short term lbl interbank']\
                              + di['long term lbl interbank'] + di['overdue liability interbank']
        di['due le:'] = di['due funds of LE'] + di['due funds state sector LE']
        di['until call:'] = di['until call funds LE'] + di['until call funds state sector LE']\
                            + di['until political parties LE']
        di['Funds of LegEnt:'] = di['due le:'] + di['until call:']
        di['Funds of PrInd:'] = di['due funds PI'] + di['until call funds PI']
        di['Accrued Expenses'] = di['MBK accrued exp'] + di['clients accrued exp'] + di['VP accrued exp']\
                                 + di['others accrued expenses']
        di['Others Liabilities'] = di['unregistered charter'] + di['dividends'] + di['others other liabilities']
        di['LIABILITIES'] = di['Interbank obl'] + di['Funds of LegEnt:'] + di['Funds of PrInd:'] \
                            + di['Savings certificates'] + di['Debt value papers'] + di['Accrued Expenses']\
                            + di['Deferred tax liability'] + di['Others Liabilities']
        di['Reserves reval MA'] = di['real estate reeval'] + di['intangibles reeval']
        # Aggregation of the PNL items
        di['% Income:'] = di['% MBK income'] + di['% income LE'] + di['% income PI'] + di['% income others']
        di['Net % Expenses'] = di['% MBK expenses'] + di['% LE expenses'] + di['% PI expenses'] + di['% other expenses']
        di['Net % Income'] = di['% Income:'] - di['Net % Expenses']
        di['Net Comiss Income'] = di['commission income'] - di['commission expenses']
        di['Trade Income'] = di['VP_income'] + di['currency and BM income']
        di['Non % income'] = di['Net Comiss Income'] + di['Trade Income'] + di['Dividends income'] + di['Capital income']\
                             + di['Other incomes']
        di['Total incomes'] = di['Net % Income'] + di['Non % income']
        di['Operational Income'] = di['Total incomes'] - (di['Administrative expenses'] + di['Personnel expenses']\
                                   + di['Losses on shares in capital'] + di['Others expenses'])
        di['Profit before tax'] = di['Operational Income'] - di['Loss on provisions']
        di['Net Profit'] = di['Profit before tax'] - di['Profit tax']
        di['This year result'] = di['Net Profit']
        # Aggregation of the Equity and Total liabilities
        di['EQUITY'] = di['Charter'] +di['Own shares'] + di['emission differences'] + di['reserves cap divid and funds']\
                       + di['Reserves reval MA'] + di['VP reevaluation'] + di['Last year result'] + di['This year result']

        di['TOTAL LIABILITIES'] = di['LIABILITIES'] + di['Subordinated debt'] + di['EQUITY']

    # perform check if there is differences between assets and liabilities amount
    diff = di['TOTAL ASSETS'] - di['TOTAL LIABILITIES']
    if diff > 0:
        print(diff, 'is a difference between Assets and Liabilities amount.')
    # extract data on the NBU rationales - N1 and N2
    name_normative = ET.parse(input("Plese enter the name of the '6F' file: "))
    root = name_normative.getroot()
    for date in root.findall('HEAD'):
        report_date = date.find('REPORTDATE').text
    for data in root.findall('DATA'):
        ekp = data.find('EKP').text
        reported_day = data.find('Q007').text
        if ekp == 'B6D001' and report_date == reported_day:
            amount = float(data.find('T100').text) / 100
            di['Regulatory capital'] = amount
        elif ekp == 'B6D002' and report_date == reported_day:
            n2_ratio = round(float(data.find('T100').text) / 100, 4)
            di['N2 ratio'] = n2_ratio

    # save extracted data in BS and PNL format to a .csv file
    name_save = str(input("Please enter the name for file to save BS and PNL data: ")) + '.csv'
    with open(name_save, 'w', newline='') as csvfile:
        fieldnames = ['Account', 'Amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for k, v in di.items():
            writer.writerow({'Account': k, 'Amount': v/100})
