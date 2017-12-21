# -*- coding: utf-8 -*-

import csv, os
import pandas as pd
from tqdm import tqdm
all_files = os.listdir('./all')
output_path = './output/large_scale_sample.csv'
time_bar = '2014-01-01'
today = '2017-12-08'

valid_stocks = []
for x in tqdm(all_files, desc = 'Searching Valid Stocks'):
    data = pd.read_csv('./all/' + x)
    if (data['Date'][0] < time_bar and data['Date'][data['Date'].size-1] == today):
        valid_stocks.append(x)

# print len(valid_stocks)
output = pd.DataFrame(columns = valid_stocks)
# print output
print len(valid_stocks)

num = 0
for stock in tqdm(valid_stocks, desc = 'Generating Data'):
    # print stock
    data = pd.read_csv('./all/' + stock)
    # print data
    data = data.loc[data['Date'] >= time_bar]
    # print data
    # diff_data = data['Close']-data['Open']
    diff_data = data['Close']
    diff_data = diff_data.reset_index(drop = True)
    # print diff_data
    # print stock
    if (diff_data.size == 993):
        output.loc[:,stock] = diff_data
    else:
        output.drop(stock, 1)
    # print output[stock]
    # break

print output
# output.to_csv('output/output.csv')
output.to_csv('output/output_close.csv')
