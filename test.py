import string
import stock.stock as stock

import tushare as ts
import UtilsTools as ut
import os
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
        stockFile = "{}/{}.h5".format(stockPath, Code)
        stockBasic.to_hdf(stockFile, "basicInfo")

        if os.getenv('DEBUG') == "TRUE":
            stockJSON = "{}/{}.json".format(stockPath, Code)
            stockBasic.to_json(stockJSON)

if __name__ == "__main__":
    #UpDataAll()
    #df = ts.get_k_data('399300', index=True, start='2016-1-01', end='2016-10-31')
    #TODO 获取历史数据的函数有变化，get-hist——data不能返回分钟数据
    df = ts.get_hist_data('600848', ktype='60', start='2016-10-01', end='2016-10-31')
    print(df)





