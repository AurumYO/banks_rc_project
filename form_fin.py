import xml.etree.ElementTree as ET
import csv

# Assets starts here
# Cash with NBU, cash, BM
cash = ['1001 A', '1002 A', '1003 A', '1004 A', '1005 A', '1007 A', '1011 A', '1012 A', '1013 A', '1017 A', '1090 П']
BM = ['1101 A', '1102 A', '1107 A', '1190 A', '1190 П']
NBU_unt_call = ['1200 A', '1207 A']
NBU_due = ['1211 A', '1212 A']
FOP = ['1203 A']
# Value Papers NBU
trade_VP_NBU = ['1400 A', '1401 A', '1402 A', '1403 A', '1404 A', '1405 A', '1405 П', '1406 A', '1406 П']
forsale_VP_NBU = ['1410 A', '1413 A', '1415 A', '1415 П', '1416 A', '1416 П']
due_rep_VP_NBU = ['1420 A', '1421 A', '1422 A', '1423 A', '1424 A', '1426 A', '1426 П']
issue_NBU = ['1430 A', '1435 A', '1435 П', '1436 A', '1436 П', '1440 A', '1446 A', '1446 П']
provis_VP_NBU = ['1419 A', '1429 A', '1419 П', '1429 П']
# Interbank
till_call = ['1500 A', '1502 A']
overn_VP = ['1510 A', '1521 A']
st_interbank = ['1512 A', '1522 A', '1523 A', '1526 A', '1526 П', '1811 A', '1819 A']
lt_interbank = ['1513 A', '1514 A', '1515 A', '1516 П', '1524 A', '1520 A', '1525 A']
overdue_interbank = ['1600 A']
provis_interbank = ['1890 П', '1509 A', '1509 П', '1519 A', '1519 П', '1529 A', '1529 П']
# Trade portfolio (value papers by fair value through PNL)
trade_port = ['3002 A', '3003 A', '3005 A', '3007 A', '3007 П', '3010 A', '3011 A', '3012 A', '3013 A', '3014 A',
              '3015 A', '3015 П', '3016 A', '3016 П', '3040 A', '3041 A', '3042 A', '3043 A', '3044 A', '3049 A']
# Portfolio for sale (VP with non fixed income by fair value via other acu. income and similar hedging assets)
port_brutto_fs = ['3102 A', '3103 A', '3105 A', '3106 A', '3107 A', '3107 П', '3110 A', '3111 A', '3112 A', '3113 A',
                  '3114 A', '3115 A', '3115 П', '3116 A', '3116 П', '3140 A', '3141 A', '3142 A', '3143 A', '3144 A']
provis_fs = ['3190 П', '3119 A', '3119 П']
# Loans , laons for l/e
bill_fact_repo_leloans = ['2010 A', '2016 A', '2016 П', '2020 A', '2026 A', '2026 П', '2030 A', '2036 A', '2036 П',
                          '2320 A', '2326 A', '2326 П', '2327 A', '2327 П', '2391 A', '2392 A', '2393 A']
corp_purpos_leloans = ['2062 A', '2063 A', '2066 A', '2066 П', '2390 A', '2396 A', '2396 П', '2397 A', '2397 П',
                       '2303 A', '2306 A', '2306 П', '2307 A', '2307 П']
investment_leloans = ['2071 A', '2076 A', '2076 П', '2394 A']
mortgage_leloans = ['2083 A', '2086 A', '2086 П', '2395 A']
overdraft_leloans = ['2600 A', '2605 A', '2650 A', '2655 A']
municipality_leloans = ['2103 A', '2106 A', '2106 П', '2113 A', '2116 A', '2116 П', '2123 A', '2126 П', '2126 A',
                        '2133 A', '2136 A', '2136 П']
overdue_deeval_leloans = ['2040 A', '2041 A', '2042 A', '2043 A', '2044 A', '2045 A', '2046 A', '2046 П', '2301 A',
                          '2321 A']
# private individuals loans
consumer_loans = ['2203 A', '2206 A', '2206 П', '2403 A', '2406 A', '2406 П', '2407 A', '2407 П']
mortgage_piloans = ['2233 A', '2236 A', '2236 П', '2433 A', '2436 A', '2436 П']
overdraft_piloans = ['2620 A', '2625 A', '3705 A']
investment_piloans = ['2211 A', '2212 A', '2213 A', '2215 A', '2216 A', '2220 A', '2226 A']
overdue_deeval_piloans = ['2401 A', '2240 A', '2241 A', '2242 A', '2243 A', '2246 A', '2246 П', '2431 A']
provisions_piloans = ['2019 A', '2019 П', '2029 A', '2029 П', '2039 A', '2039 П', '2049 П', '2069 A', '2069 П',
                      '2079 A', '2079 П', '2089 A', '2089 П', '2109 A', '2109 П', '2119 A', '2119 П', '2129 A',
                      '2129 П', '2139 A', '2139 П', '2209 A', '2209 П', '2219 A', '2219 П', '2229 A', '2229 П',
                      '2309 A', '2309 П', '2329 A', '2329 П', '2239 A', '2239 П', '2249 A', '2249 П', '2409 П',
                      '2409 A', '2439 П', '2439 A', '2609 П', '2609 A', '2629 A', '2629 П', '2659 П', '2659 A',
                      '2049 A']
# valued papers due to payment
port_brutto_vp = ['3210 A', '3211 A', '3212 A', '3213 A', '3214 A', '3216 A', '3216 П']
provisions_vp = ['3219 П', '3219 A']
# Investments in SC and Associates
investment_sc_associates = ['4102 A', '4103 A', '4105 A', '4202 A', '4203 A', '4205 A']
# main assets
main_assets = ['4400 A', '4409 П', '4410 A', '4419 П', '4430 A', '4431 A', '4500 A', '4509 П', '4530 A', '4600 A',
               '4600 П', '4609 A', '4609 П']
# intangibles
intagibl = ['4300 A', '4309 П', '4310 A', '4321 A']
# accrued income
mbk_ai = ['1208 A', '1218 A', '1508 A', '1508 П', '1518 A', '1528 A']
vp_ai = ['1408 A', '1418 A', '1428 A', '1438 A', '1448 A', '3008 A', '3018 A', '3108 A', '3118 A', '3128 A', '3138 A',
         '3218 A', '4208 A']
le_ai = ['2018 A', '2018 П', '2028 A', '2028 П', '2038 A', '2038 П', '2048 П', '2048 A', '2068 A', '2068 П', '2078 A',
         '2078 П', '2088 A', '2088 П', '2128 A', '2108 A', '2118 A', '2118 П', '2308 A', '2328 A', '2398 A', '2607 A',
         '2657 A', '3570 A', '3578 A']
pi_ai = ['2208 A', '2208 П', '2218 A', '2228 A', '2238 A', '2238 П', '2248 A', '2627 A', '2248 П', '2408 A', '2438 A']
overdue_income_ai = []
overdue_income_ai2 = []
provisions_ai = []
# deferred tax
deferred_tax = ['3521 A']
# other assets
account_payables = ['2800 A', '2801 A', '2802 A', '2805 A', '2806 A', '2809 A', '2920 A', '2924 A']
other_assets = ['3400 A', '3402 A', '3403 A', '3407 A', '3500 A', '3510 A', '3519 A', '3520 A', '3522 A', '3540 A',
                '3541 A', '3542 A', '3548 A', '3550 A', '3551 A', '3552 A', '3559 A', '3739 A', '3710 A', '3900 A',
                '3902 A', '3906 A', '3904 A', '3800 A', '3801 П', '3901 A', '3413 A']
provisions_oa = ['2890 П', '3590 П', '3599 П']
# long term assets for sale
lt_assets_for_sale = ['3122 A', '3123 A', '3125 A', '3132 A', '3133 A', '3135 A', '3408 A', '3409 A']
# Liabilities starts here
# interbank util call
until_call_interbank = ['1300 П', '1600 П', '1602 П']
overnight_interbank = ['1310 П', '1500 П', '1610 П', '1621 П']
shortterm_liab_interbank = ['1311 П', '1312 П', '1313 П', '1316 П', '1332 П', '1612 П', '1622 П', '1623 П', '1626 П',
                            '1626 A', '1911 П', '1919 П', '1316 A']
longterm_liab_interbank = ['1322 П', '1323 П', '1324 П', '1325 П', '1326 П', '1326 A', '1335 П', '1613 П', '1615 П',
                           '1624 П']
overdue_liab_interbank = []
# funds of legal entities
due_funds_le = ['2610 П', '2611 П', '2615 П', '2616 A', '2616 П', '2617 П', '2651 П', '2652 П', '2700 П', '2701 П',
                '2706 A', '2706 П', '2707 П']
due_statesect_le = ['2525 П', '2546 П', '2551 П']
untillcall_funds_le = ['2600 П', '2601 П', '2602 П', '2603 П', '2604 П', '2605 П', '2606 П', '2650 П', '2653 П',
                       '2655 П', '2654 П', '2656 A', '2656 П', '2900 П', '2901 П', '2902 П', '2903 П', '2904 П',
                       '2905 П', '2906 П', '2909 П']
untilcall_statesect_le = ['2512 П', '2513 П', '2520 П', '2523 П', '2526 П', '2530 П', '2531 П', '2541 П', '2542 П',
                          '2544 П', '2545 П', '2552 П', '2550 П', '2553 П', '2554 П', '2555 П', '2556 П', '2560 П',
                          '2561 П', '2562 П', '2565 П', '2570 П', '2571 П', '2572 П']
untilcall_polpatry_le = ['2640 П', '2641 П', '2642 П', '2643 П']
# funds private individuals
due_funds_pi = ['2630 П', '2635 П', '2636 A', '2636 П', '2637 П']
untcall_funds_pi = ['2620 П', '2622 П', '2625 П', '2920 П', '2924 П', '3705 П']
# savings certificates
saving_certif = ['3320 П', '3326 П', '3326 A', '3327 П', '3330 П', '3336 П', '3337 П', '3340 П', '3346 П', '3347 П']
# debt VP
debt_vp = ['3300 П', '3301 П', '3305 П', '3306 П', '3307 П', '3310 П', '3311 П', '3315 П', '3316 П', '3317 П', '3350 П',
           '3351 П', '3352 П', '3353 П', '3354 П', '3359 П', '3360 П', '3361 П', '3362 П']
# accrued expenses
mbk_ae = ['1308 П', '1318 П', '1328 П', '1338 П', '1507 П', '1608 П', '1618 П', '1628 П']
clients_ae = ['2518 П', '2528 П', '2538 П', '2548 П', '2558 П', '2568 П', '2608 П', '2618 П', '2628 П', '2638 П',
              '2658 П', '2708 A', '2708 П']
vp_ae = ['3308 П', '3318 П', '3328 П', '3338 П', '3348 П']
others_ae = ['3668 П', '3678 П', '3670 П']
# Deferred tax liability
deferred_tax_liabl = ['3621 П']
# other liabilities
unregist_chart = ['3630 П']
dividends = ['3631 П']
other_other_liabl = ['2908 П', '3600 П', '3610 П', '3615 П', '3607 П', '3619 П', '3620 П', '3622 П', '3623 П', '3641 П',
                     '3640 П', '3642 П', '3648 П', '3652 П', '3650 П', '3651 П', '3654 П', '3653 П', '3658 П', '3659 П',
                     '3690 П', '3692 П', '3699 П', '3720 П', '3739 П', '3800 П', '3801 A', '3900 П', '3901 П', '3903 П',
                     '3905 П', '3907 П', '3618 П', '3611 П']
# subordinated debt
subord_debt = ['3660 П', '3666 A', '3667 П']
# charter and equity
charter = ['5000 П', '5001 П', '5004 П']
own_shares = ['5002 П', '5002 A']
emission_diff = ['5010 П', '5011 П', '5011 A']
prov_capdivid_funds = ['5003 П', '5020 П', '5021 П', '5022 П']
# reevaluation of the assets
realest_reeval = ['5100 П']
intangibl_reeval = ['5101 П']
vp_reeval = ['5102 A', '5102 П', '5103 П', '5104 П', '5105 П', '5105 A', '5106 A', '5107 П']
# Last year result
ly_result = ['5030 П', '5031 A', '5040 П', '5041 A']
# PNL starts here
# Net income
net_perc_income = ['6000 П', '6002 П', '6003 П', '6010 П', '6011 П', '6012 П', '6013 П', '6013 A', '6014 П', '6015 П',
                   '6016 П', '6017 П', '6018 П', '6019 П']
net_le_income = ['6020 П', '6021 П', '6022 П', '6022 A', '6023 П', '6024 П', '6024 A', '6025 П', '6025 A', '6026 П',
                 '6026 A', '6027 П', '6027 A', '6029 П', '6030 П', '6031 П', '6032 П', '6033 П', '6033 A', '6034 П',
                 '6034 A', '6035 П', '6040 П', '6041 П', '6042 П', '6042 A', '6043 П', '6044 П', '6045 П', '6046 П',
                 '6046 A', '6047 П', '6070 A']
net_pi_income = ['6050 A', '6050 П', '6052 П', '6052 A', '6053 П', '6054 П', '6055 П', '6055 A', '6060 П', '6060 A',
                 '6061 П', '6061 A', '6062 П', '6062 A', '6063 П', '6063 A', '6104 П', '6110 П', '6111 П', '6112 П',
                 '6113 П']
net_other_income = ['6051 П', '6051 A', '6056 П', '6090 П', '6099 П', '6120 П', '6121 П', '6121 A', '6122 П', '6123 П', '6124 П',
                    '6124 A', '6125 П', '6126 A', '6126 П', '6127 П', '6128 П', '6130 П', '6140 П', '6141 П', '6100 A',
                    '6100 П', '6103 П', '6128 A']
# Net expenses
mbk_net_exp = ['7000 A', '7002 A', '7003 A', '7004 A', '7005 A', '7006 A', '7010 A', '7011 A', '7012 A', '7013 A',
               '7014 A', '7015 A', '7016 A', '7017 A']
le_net_exp = ['7020 A', '7020 П', '7021 A', '7021 П', '7028 A', '7028 П', '7030 A', '7030 П', '7060 A', '7060 П',
              '7061 A', '7061 П', '7070 A', '7070 П', '7071 A', '7071 П']
pi_net_exp = ['7040 A', '7041 A', '7040 П', '7041 П']
other_net_exp = ['7096 A', '7099 A', '7120 A', '7121 A', '7122 A', '7123 A', '7124 A', '7125 A', '7130 A', '7140 A',
                 '7141 A']
# net commission income
commiss_income = ['6108 П', '6109 П', '6114 П', '6116 П', '6118 П', '6119 П', '6500 П', '6501 П', '6503 П', '6504 П',
                  '6506 П', '6508 П', '6509 П', '6510 П', '6511 П', '6513 П', '6514 П', '6516 П', '6518 П', '6519 П',
                  '6520 П']
commiss_expenses = ['7100 A', '7103 A', '7104 A', '7108 A', '7109 A', '7500 A', '7501 A', '7503 A', '7504 A', '7506 A',
                    '7508 A', '7509 A', '7520 A']
# trade income
vp_income = ['6201 П', '6201 A', '6203 П', '6203 A', '6205 П', '6205 A', '6206 П', '6206 A', '6207 П', '6207 A',
             '6209 П', '6209 A', '6211 П', '6211 A', '6218 П', '6218 A', '6223 П', '6223 A']
curren_bm_income = ['6204 П', '6204 A', '6208 П', '6208 A', '6214 П', '6214 A', '6215 П', '6215 A', '6216 П', '6216 A',
                    '6217 П', '6217 A', '6219 П', '6219 A']
# dividends income
dividends_income = ['6300 П', '6301 П', '6302 П', '6303 П']
# Capital income
capital_income = ['6310 П', '6311 П']
# Other incomes
other_incomes = ['6224 П', '6224 A', '6225 П', '6225 A', '6226 П', '6226 A', '6320 П', '6330 П', '6340 П', '6350 П',
                 '6380 П', '6390 П', '6391 П', '6391 A', '6392 П', '6392 A', '6393 П', '6393 A', '6394 П', '6395 П',
                 '6396 П', '6397 П', '6398 П', '6399 П', '6490 П', '6499 П', '6710 П', '6711 П', '6712 П', '6713 П',
                 '6714 П', '6715 П', '6717 П']
# Administrative expenses
admin_expenses = ['7300 A', '7301 A', '7410 A', '7411 A', '7418 A', '7419 A', '7420 A', '7421 A', '7423 A', '7424 A', '7430 A',
                  '7431 A', '7432 A', '7433 A', '7440 A', '7441 A', '7442 A', '7450 A', '7452 A', '7454 A', '7455 A',
                  '7456 A', '7457 A']
# Personel expenses
personel_expenses = ['7400 A', '7401 A', '7403 A', '7404 A', '7405 A', '7409 A']
# Losses on capital
loss_on_capital = ['7310 A', '7311 A']
# others expenses
others_expenses = ['7320 A', '7340 A', '7380 A', '7390 A', '7391 A', '7392 A', '7394 A', '7395 A', '7396 A', '7397 A',
                   '7398 A', '7399 A', '7809 A', '7499 A', '7490 A', '7491 A', '7491 П', '7499 П', '7399 П', '7350 A']
# Loss on forming provisions
loss_on_provision = ['7700 П', '7701 П', '7702 П', '7703 П', '7704 П', '7705 П', '7706 П', '7707 П', '7700 A', '7701 A',
                     '7702 A', '7703 A', '7704 A', '7705 A', '7706 A', '7707 A', '7720 A', '7720 П']
# Profit tax
profit_tax = ['7900 A', '7900 П']
# remaining accounts
remain_accounts = []

# BS and PNL dictionary
di = {'Cash in NBU cash and BM': 0, 'Cash': 0, 'BM': 0, 'NBU until call': 0, 'NBU due': 0, 'FOP': 0,
      'VP NBU': 0, 'Trade VP NBU': 0, 'For sale VP NBU': 0, 'Due to payment VP NBU': 0, 'Issue NBU': 0,
      'Provisions VP NBU': 0, 'Interbank': 0, 'Until request': 0, 'Overnight': 0, 'S/T interbank': 0,
      'L/T interbank': 0, 'Overdue interbank': 0, 'Provisions interbank': 0, 'Trade portfolio (FV)': 0,
      'Portfolio for sale': 0, 'Portfolio-brutto': 0, 'Provisions (Portfolio for sale)': 0, 'Loans:': 0,
      'Legal entities loans': 0, 'bills factoring repo (loans to l/e)': 0, 'corporate purposes (loans to l/e)': 0,
      'investment loans (loans to l/e)': 0, 'mortgage loans to l/e': 0, 'overdrafts to l/e': 0, 'municipality loans': 0,
      'overdue/devaluated loans to l/e': 0, 'Private individ loans': 0, 'consumer loans PI': 0, 'mortgage PI': 0,
      'overdraft PI': 0, 'to investments activity': 0, 'overdue/devaluated PI': 0, 'provisions PI loans': 0,
      'VP due to repayment': 0, 'portfolio brutto VP': 0, 'provisions VP': 0, 'Investments to sub and associates': 0,
      'Main assets': 0, 'Intangibles': 0, 'Accrued income':0, 'MBK AI': 0, 'VP AI': 0, 'LE AI': 0, 'PI AI': 0,
      'overdue income AI': 0, 'overdue income2 AI': 0, 'provisions AI': 0, 'Deferred tax': 0, 'Others assets': 0,
      'account payables': 0, 'other assets': 0, 'provisions other assets': 0, 'LT asset for sale': 0, 'TOTAL ASSETS': 0,
      'Interbank obl': 0,'until call interbank': 0, 'overnight interbank': 0, 'short term lbl interbank': 0,
      'long term lbl interbank': 0, 'overdue liability interbank': 0, 'Funds of LegEnt:':0, 'due le:': 0,
      'due funds of LE': 0, 'due funds state sector LE': 0, 'until call:': 0, 'until call funds LE': 0,
      'until call funds state sector LE': 0, 'until political parties LE': 0, 'Funds of PrInd:': 0, 'due funds PI': 0,
      'until call funds PI': 0, 'Savings certificates': 0, 'Debt value papers': 0, 'Accrued Expenses': 0,
      'MBK accrued exp': 0, 'clients accrued exp': 0, 'VP accrued exp': 0, 'others accrued expenses': 0,
      'Deferred tax liability': 0, 'Others Liabilities': 0, 'unregistered charter': 0, 'dividends': 0,
      'others other liabilities': 0, 'LIABILITIES': 0, 'Subordinated debt': 0, 'Charter': 0,
      'Own shares': 0, 'emission differences': 0, 'reserves cap divid and funds': 0, 'Reserves reval MA': 0,
      'real estate reeval': 0, 'intangibles reeval': 0, 'VP reevaluation': 0, 'Last year result': 0,
      'This year result': 0, 'EQUITY': 0, 'TOTAL LIABILITIES': 0,
      'Net % Income': 0, '% Income:': 0, '% MBK income': 0, '% income LE': 0, '% income PI': 0,
      '% income others': 0, 'Net % Expenses': 0, '% MBK expenses': 0, '% LE expenses': 0, '% PI expenses': 0,
      '% other expenses': 0, 'Net Comiss Income': 0, 'commission income': 0, 'commission expenses': 0,
      'Trade Income': 0, 'VP_income': 0, 'currency and BM income': 0, 'Dividends income': 0, 'Capital income': 0,
      'Other incomes': 0, 'Non % income':0, 'Total incomes': 0, 'Administrative expenses': 0, 'Personel expenses': 0,
      'Losses on shares in capital': 0, 'Others expenses': 0, 'Operational Income': 0, 'Loss on provisions': 0,
      'Profit before tax': 0, 'Profit tax': 0, 'Net Profit': 0}

name = str(input("Please enter the file: "))

for data in csv.DictReader(open(name), delimiter=','):
    # cash with NBU
    if str(data['Account']) in cash:
        di['Cash'] += float(data['Amount'])
    if str(data['Account']) in BM:
        di["BM"] += float(data['Amount'])
    if str(data['Account']) in NBU_unt_call:
        di["NBU until call"] += float(data['Amount'])
    if str(data['Account']) in NBU_due:
        di["NBU due"] += float(data['Amount'])
    if str(data['Account']) in FOP:
        di["FOP"] += float(data['Amount'])
    # Value Papers NBU
    if str(data['Account']) in trade_VP_NBU:
        di["Trade VP NBU"] += float(data['Amount'])
    if str(data['Account']) in forsale_VP_NBU:
        di["For sale VP NBU"] += float(data['Amount'])
    if str(data['Account']) in due_rep_VP_NBU:
        di["Due to payment VP NBU"] += float(data['Amount'])
    if str(data['Account']) in issue_NBU:
        di["Issue NBU"] += float(data['Amount'])
    if str(data['Account']) in provis_VP_NBU:
        di["Provisions VP NBU"] += float(data['Amount'])
    # Interbank
    if str(data['Account']) in till_call:
        di["Until request"] += float(data['Amount'])
    if str(data['Account']) in overn_VP:
        di["Overnight"] += float(data['Amount'])
    if str(data['Account']) in st_interbank:
        di["S/T interbank"] += float(data['Amount'])
    if str(data['Account']) in lt_interbank:
        di["L/T interbank"] += float(data['Amount'])
    if str(data['Account']) in overdue_interbank:
        di["Overdue interbank"] += float(data['Amount'])
    if str(data['Account']) in provis_interbank:
        di["Provisions interbank"] += float(data['Amount'])
    # Trade portfolio - Value papers by fair value
    if str(data['Account']) in trade_port:
        di["Trade portfolio (FV)"] += float(data['Amount'])
    # Portfolio fo sale
    if str(data['Account']) in port_brutto_fs:
        di["Portfolio-brutto"] += float(data['Amount'])
    if str(data['Account']) in provis_fs:
        di["Provisions (Portfolio for sale)"] += float(data['Amount'])
    # Loans legal entities
    if str(data['Account']) in bill_fact_repo_leloans:
        di["bills factoring repo (loans to l/e)"] += float(data['Amount'])
    if str(data['Account']) in corp_purpos_leloans:
        di["corporate purposes (loans to l/e)"] += float(data['Amount'])
    if str(data['Account']) in investment_leloans:
        di["investment loans (loans to l/e)"] += float(data['Amount'])
    if str(data['Account']) in mortgage_leloans:
        di["mortgage loans to l/e"] += float(data['Amount'])
    if str(data['Account']) in overdraft_leloans:
        di["overdrafts to l/e"] += float(data['Amount'])
    if str(data['Account']) in municipality_leloans:
        di["municipality loans"] += float(data['Amount'])
    if str(data['Account']) in overdue_deeval_leloans:
        di["overdue/devaluated loans to l/e"] += float(data['Amount'])
    # Loans private individuals
    if str(data['Account']) in consumer_loans:
        di["consumer loans PI"] += float(data['Amount'])
    if str(data['Account']) in mortgage_piloans:
        di["mortgage PI"] += float(data['Amount'])
    if str(data['Account']) in overdraft_piloans:
        di["overdraft PI"] += float(data['Amount'])
    if str(data['Account']) in investment_piloans:
        di["to investments activity"] += float(data['Amount'])
    if str(data['Account']) in overdue_deeval_piloans:
        di["overdue/devaluated PI"] += float(data['Amount'])
    if str(data['Account']) in provisions_piloans:
        di["provisions PI loans"] += float(data['Amount'])
    # Valued papaers due to repayment
    if str(data['Account']) in port_brutto_vp:
        di["portfolio brutto VP"] += float(data['Amount'])
    if str(data['Account']) in provisions_vp:
        di["provisions VP"] += float(data['Amount'])
    # Investments in SC and Associates
    if str(data['Account']) in investment_sc_associates:
        di["Investments to sub and associates"] += float(data['Amount'])
    # Main assets
    if str(data['Account']) in main_assets:
        di["Main assets"] += float(data['Amount'])
    # Intangibles
    if str(data['Account']) in intagibl:
        di["Intangibles"] += float(data['Amount'])
    # accrued income
    if str(data['Account']) in mbk_ai:
        di["MBK AI"] += float(data['Amount'])
    if str(data['Account']) in vp_ai:
        di["VP AI"] += float(data['Amount'])
    if str(data['Account']) in le_ai:
        di["LE AI"] += float(data['Amount'])
    if str(data['Account']) in pi_ai:
        di["PI AI"] += float(data['Amount'])
    if str(data['Account']) in overdue_income_ai:
        di["overdue income AI"] += float(data['Amount'])
    if str(data['Account']) in overdue_income_ai2:
        di["overdue income2 AI"] += float(data['Amount'])
    if str(data['Account']) in provisions_ai:
        di["provisions AI"] += float(data['Amount'])
    # deffered tax
    if str(data['Account']) in deferred_tax:
        di["Deferred tax"] += float(data['Amount'])
    # other assets
    if str(data['Account']) in account_payables:
        di["account payables"] += float(data['Amount'])
    if str(data['Account']) in other_assets:
        di["other assets"] += float(data['Amount'])
    if str(data['Account']) in provisions_oa:
        di["provisions other assets"] += float(data['Amount'])
    # long term assets for sale
    if str(data['Account']) in lt_assets_for_sale:
        di["LT asset for sale"] += float(data['Amount'])
    # LIABILITIES section
    # Interbank until call
    if str(data['Account']) in until_call_interbank:
        di["until call interbank"] += float(data['Amount'])
    if str(data['Account']) in overnight_interbank:
        di["overnight interbank"] += float(data['Amount'])
    if str(data['Account']) in shortterm_liab_interbank:
        di["short term lbl interbank"] += float(data['Amount'])
    if str(data['Account']) in longterm_liab_interbank:
        di["long term lbl interbank"] += float(data['Amount'])
    if str(data['Account']) in overdue_liab_interbank:
        di["overdue liability interbank"] += float(data['Amount'])
    # funds of legal entities
    if str(data['Account']) in due_funds_le:
        di["due funds of LE"] += float(data['Amount'])
    if str(data['Account']) in due_statesect_le:
        di["due funds state sector LE"] += float(data['Amount'])
    if str(data['Account']) in untillcall_funds_le:
        di["until call funds LE"] += float(data['Amount'])
    if str(data['Account']) in untilcall_statesect_le:
        di["until call funds state sector LE"] += float(data['Amount'])
    if str(data['Account']) in untilcall_polpatry_le:
        di["until political parties LE"] += float(data['Amount'])
# funds private individuals
    if str(data['Account']) in due_funds_pi:
        di["due funds PI"] += float(data['Amount'])
    if str(data['Account']) in untcall_funds_pi:
        di["until call funds PI"] += float(data['Amount'])
# savings certificates
    if str(data['Account']) in saving_certif:
        di["Savings certificates"] += float(data['Amount'])
# debt VP
    if str(data['Account']) in debt_vp:
        di["Debt value papers"] += float(data['Amount'])
# accrued expenses
    if str(data['Account']) in mbk_ae:
        di["MBK accrued exp"] += float(data['Amount'])
    if str(data['Account']) in clients_ae:
        di["clients accrued exp"] += float(data['Amount'])
    if str(data['Account']) in vp_ae:
        di["VP accrued exp"] += float(data['Amount'])
    if str(data['Account']) in others_ae:
        di["others accrued expenses"] += float(data['Amount'])
# deferred tax liability
    if str(data['Account']) in deferred_tax_liabl:
        di["Deferred tax liability"] += float(data['Amount'])
# Other liabilities
    if str(data['Account']) in unregist_chart:
        di["unregistered charter"] += float(data['Amount'])
    if str(data['Account']) in dividends:
        di["dividends"] += float(data['Amount'])
    if str(data['Account']) in other_other_liabl:
        di["others other liabilities"] += float(data['Amount'])
# subordinated debt
    if str(data['Account']) in subord_debt:
        di["Subordinated debt"] += float(data['Amount'])
# charter and equity
    if str(data['Account']) in charter:
        di["Charter"] += float(data['Amount'])
    if str(data['Account']) in own_shares:
        di["Own shares"] += float(data['Amount'])
    if str(data['Account']) in emission_diff:
        di["emission differences"] += float(data['Amount'])
    if str(data['Account']) in prov_capdivid_funds:
        di["reserves cap divid and funds"] += float(data['Amount'])
# provisions reevalutioans
    if str(data['Account']) in realest_reeval:
        di["real estate reeval"] += float(data['Amount'])
    if str(data['Account']) in intangibl_reeval:
        di["intangibles reeval"] += float(data['Amount'])
    if str(data['Account']) in vp_reeval:
        di["VP reevaluation"] += float(data['Amount'])
# Last year result
    if str(data['Account']) in ly_result:
        di["Last year result"] += float(data['Amount'])
# PNL starts here
# Net income
    if str(data['Account']) in net_perc_income:
        di["% MBK income"] += float(data['Amount'])
    if str(data['Account']) in net_le_income:
        di["% income LE"] += float(data['Amount'])
    if str(data['Account']) in net_pi_income:
        di["% income PI"] += float(data['Amount'])
    if str(data['Account']) in net_other_income:
        di["% income others"] += float(data['Amount'])
# Net expenses
    if str(data['Account']) in mbk_net_exp:
        di["% MBK expenses"] += float(data['Amount'])
    if str(data['Account']) in le_net_exp:
        di["% LE expenses"] += float(data['Amount'])
    if str(data['Account']) in pi_net_exp:
        di["% PI expenses"] += float(data['Amount'])
    if str(data['Account']) in other_net_exp:
        di["% other expenses"] += float(data['Amount'])
# net commission income
    if str(data['Account']) in commiss_income:
        di["commission income"] += float(data['Amount'])
    if str(data['Account']) in commiss_expenses:
        di["commission expenses"] += float(data['Amount'])
# trade income
    if str(data['Account']) in vp_income:
        di["VP_income"] += float(data['Amount'])
    if str(data['Account']) in curren_bm_income:
        di["currency and BM income"] += float(data['Amount'])
# dividends income
    if str(data['Account']) in dividends_income:
        di["Dividends income"] += float(data['Amount'])
# Capital income
    if str(data['Account']) in capital_income:
        di["Capital income"] += float(data['Amount'])
# Other incomes
    if str(data['Account']) in other_incomes:
        di["Other incomes"] += float(data['Amount'])
# Administrative expenses
    if str(data['Account']) in admin_expenses:
        di["Administrative expenses"] += float(data['Amount'])
# Personel expenses
    if str(data['Account']) in personel_expenses:
        di["Personel expenses"] += float(data['Amount'])
# Losses on capital participation
    if str(data['Account']) in loss_on_capital:
        di["Losses on shares in capital"] += float(data['Amount'])
# Other expenses
    if str(data['Account']) in others_expenses:
        di["Others expenses"] += float(data['Amount'])
# Net losses on provisions
    if str(data['Account']) in loss_on_provision:
        di["Loss on provisions"] += float(data['Amount'])
# Profit taxt
    if str(data['Account']) in profit_tax:
        di["Profit tax"] += float(data['Amount'])

# remaining accounts
#     if str(data['Account']) not in :
#         remain_accounts.append(data['Account'])
# print(di)

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
    di['until call:'] = di['until call funds LE'] + di['until call funds state sector LE'] + di['until political parties LE']
    di['Funds of LegEnt:'] = di['due le:'] + di['until call:']
    di['Funds of PrInd:'] = di['due funds PI'] + di['until call funds PI']
    di['Accrued Expenses'] = di['MBK accrued exp'] + di['clients accrued exp'] + di['VP accrued exp'] + di['others accrued expenses']
    di['Others Liabilities'] = di['unregistered charter'] + di['dividends'] + di['others other liabilities']
    di['LIABILITIES'] = di['Interbank obl'] + di['Funds of LegEnt:'] + di['Funds of PrInd:']\
                              + di['Savings certificates'] + di['Debt value papers'] + di['Accrued Expenses']\
                              + di['Deferred tax liability'] + di['Others Liabilities']
    di['Reserves reval MA'] = di['real estate reeval'] + di['intangibles reeval']
    # Agregation of the PNL items
    di['% Income:'] = di['% MBK income'] + di['% income LE'] + di['% income PI'] + di['% income others']
    di['Net % Expenses'] = di['% MBK expenses'] + di['% LE expenses'] + di['% PI expenses'] + di['% other expenses']
    di['Net % Income'] = di['% Income:'] - di['Net % Expenses']
    di['Net Comiss Income'] = di['commission income'] - di['commission expenses']
    di['Trade Income'] = di['VP_income'] + di['currency and BM income']
    di['Non % income'] = di['Net Comiss Income'] + di['Trade Income'] + di['Dividends income'] + di['Capital income']\
                         + di['Other incomes']
    di['Total incomes'] = di['Net % Income'] + di['Non % income']
    di['Operational Income'] = di['Total incomes'] - (di['Administrative expenses'] + di['Personel expenses']\
                               + di['Losses on shares in capital'] + di['Others expenses'])
    di['Profit before tax'] = di['Operational Income'] - di['Loss on provisions']
    di['Net Profit'] = di['Profit before tax'] - di['Profit tax']
    di['This year result'] = di['Net Profit']
    # Agregation of the Equity and Total liabililties
    di['EQUITY'] = di['Charter'] +di['Own shares'] + di['emission differences'] + di['reserves cap divid and funds']\
                   + di['Reserves reval MA'] + di['VP reevaluation'] + di['Last year result'] + di['This year result']
    di['TOTAL LIABILITIES'] = di['LIABILITIES'] + di['Subordinated debt'] + di['EQUITY']


# print(di['TOTAL ASSETS'], 'total assets')
# print(di['TOTAL LIABILITIES'], 'total assets')
diff = di['TOTAL ASSETS'] - di['TOTAL LIABILITIES']
print(diff, 'difference')

# obligatory normative extraction
name_normative = ET.parse(input("Plese enter the name of the '6F' file: "))
root = name_normative.getroot()
for date in root.findall('HEAD'):
    report_date = date.find('REPORTDATE').text

for data in root.findall('DATA'):
    ekp = data.find('EKP').text
    reported_day = data.find('Q007').text
    if ekp == 'B6D001' and report_date == reported_day:
        amount = float(data.find('T100').text)/100
        di['Regulatory capital'] = amount
        print(di['Regulatory capital'], 'Regulatory capital')
    elif ekp == 'B6D002' and report_date == reported_day:
        n2_ratio = round(float(data.find('T100').text)/100, 4)
        di['N2 ratio'] = n2_ratio
        print(di['N2 ratio'], 'N2')

# writing the recieved data to new file
name_save = str(input("Please enter the name for BS and PNL data: ")) + '.csv'
with open(name_save, 'w', newline='') as csvfile:
    fieldnames = ['Account', 'Amount']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for k, v in di.items():
        writer.writerow({'Account': k, 'Amount': v})
