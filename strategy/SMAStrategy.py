#策略 Simple Moving Average (SMA)
#策略参考如下
#https://tradingsim.com/blog/simple-moving-average/


import backtrader as bt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


from common.TushareLoader import TushareLoader

#类名后面的括号代表是的是继承的意思
class SMAStrategy(bt.Strategy):
    def __init__(self):
        print('进入初始化方法')
        #print(type(self)) self是主线程进来的，这个类的实例 <class '__main__.SMAStrategy'>

        self.dataclose = self.data0.close
        self.order = None
        self.buyprice = None
        self.buycomm = None

        self.sma = bt.indicators.SimpleMovingAverage(self.data0,period=5)


    def next(self):
        print('进入next方法')


    def notify_order(self, order):
        print('进入notify_order方法')

    def notify_trade(self, trade):
        print("进入notify_trade方法")

    def log(self,txt,dt=None,doprint=False):
        if doprint:
            dt = dt or self.datas[0].datetime.date[0]
            print('%s, %s' % (dt.isoformat(),txt) )


if __name__ == '__main__':

    tsLoader = TushareLoader()
    dataFrame = tsLoader.getDailyBar('601211.SH','20210101','20220211')
    print(dataFrame)
    dataFrame['Datetime'] = pd.to_datetime(dataFrame['trade_date'])
    dataFrame.set_index('Datetime',inplace=True)
    feed = bt.feeds.PandasData(dataname=dataFrame)


    cerebro = bt.Cerebro()
    cerebro.adddata(feed)

    cerebro.addstrategy(SMAStrategy)

    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='SharpeRatio')
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name='DrawDown')

    cerebro.broker.setcash(10000)
    cerebro.broker.setcommission(commission=0.0005)

    cerebro.addsizer(bt.sizers.PercentSizer, percents=90)
    result = cerebro.run()

    aa = result[0].analyzers.SharpeRatio.get_analysis();

    print('夏普比率：',result[0].analyzers.SharpeRatio.get_analysis()['sharperatio'])
    print('最大回撤：',result[0].analyzers.DrawDown.get_analysis()['max']['drawdown'])
    cerebro.plot()