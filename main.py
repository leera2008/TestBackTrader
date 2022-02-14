import backtrader as bt
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np

if __name__ == '__main__':
    cerebro = bt.Cerebro()
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.run()
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())