import tushare as ts
import pandas as pd
from common.ConfigLoader import ConfigLoader

#从tushare获取数据
class TushareLoader(object):

    def __init__(self):
        config = ConfigLoader().getConfig()
        ts.set_token(config['Tushare']['token'])
        self.pro = ts.pro_api()

    #获取日线行情，没有复权，原始值
    def getDailyBar(self,code,startDate,endDate):
        df = self.pro.daily(ts_code=code, start_date=startDate, end_date=endDate)
        return df





if __name__ == '__main__':
    # 打印版本
    print(ts.__version__)

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('max_colwidth', 10000)
    pd.set_option('display.width', 10000)

    tsLoader = TushareLoader()
    df = tsLoader.getDailyBar('601211.SH','20210101','20220211')
    print(type(df))
    print(df)
