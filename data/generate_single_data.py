import fix_yahoo_finance as yf
import csv

x = 'AAPL'
data = yf.download(x, start='2014-09-19')
print "Data Size = " + str(data.size) + "\n"
print data

if data.size != 0:
    data.to_csv('single/'+x+'.csv')
else:
    print "NULL DATA"
