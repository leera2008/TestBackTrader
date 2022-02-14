import pandas as pd
from common.ConfigLoader import ConfigLoader
from common.TushareLoader import TushareLoader

config = ConfigLoader().getConfig()
tsLoader = TushareLoader()
tsLoader.getDailyBar()

#查询当前所有正常上市交易的股票列表
data = pro.stock_basic(exchange='',ts_code='601211.SH', list_status='L', fields='ts_code,symbol,name,area,industry,list_date',limit=1)
print(data)


#获取不复权的日线行情
# df1 = pro.daily(ts_code='601211.SH', start_date='20210101', end_date='20220211')
# print(df1)

#取得后复权日线行情
#df = ts.pro_bar(ts_code='601211.SH', adj='hfq', start_date='20210101', end_date='20220211')
#print(df)


#取得一天的全部历史
df = pro.daily(ts_code='601211.SH',trade_date='20180810')
print(df)


