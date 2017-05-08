import string
import stock.stock as stock

import tushare as ts
import UtilsTools as ut
import os
import matplotlib.pyplot as plt
import pandas as pd

stockDict = []

def UpDataAll():
    df = ts.get_stock_basics()

    for Code in df.index:
        stockObj = stock.stockObject(df.ix[Code])
        stockDict[Code] = stockObj

        stockPath = ut.getStockPath(Code)
        ut.checkdir(stockPath)
        stockBasic = df.ix[Code]
        stockFile = "{}/{}.csv".format(stockPath, Code)
        stockBasic.to_csv(stockFile, index=False)

if __name__ == "__main__":
    #UpDataAll()
    df_d = ts.get_k_data('600100', ktype='D')

    #计算5、20、60、120、250日算术平均线
    ma_list = [5, 20, 60, 120, 250]
    for ma in ma_list:
        df_d['MA_' + str(ma)] = df_d['close'].rolling(center=False, window=ma).mean()

    # 计算5、20、60、120、250日指数平均线
    for ma in ma_list:
        df_d['EMA_' + str(ma)] = df_d['close'].ewm(span=ma, ignore_na=False, adjust=True).mean()

    print(df_d)






