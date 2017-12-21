# -*- coding: utf-8 -*-

import pandas as pd

x = 'AAPL'
file_path = 'single/'+x+'.csv'
data = pd.read_csv(file_path)
diff_data = data['Close']-data['Open']
# diff_data = data['Close']

diff_data = diff_data.reset_index(drop = True)
print diff_data
diff_data.to_csv('output/'+x+'.csv',index=False)
# diff_data.to_csv('output/'+x+'_close.csv',index=False)
