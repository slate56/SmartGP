import string

import tushare as ts
import UtilsTools as ut
import os


def UpDataAll():
    import pandas as pd

    df = ts.get_stock_basics()

    for stockCode in df.index:
        stockPath = ut.getStockPath(stockCode)
        ut.mkdir(stockPath)
        stockBasic = df.ix[stockCode]
        stockFile = "{}/{}.h5".format(stockPath, stockCode)
        stockBasic.to_hdf(stockFile, "basicInfo")

        if os.getenv('DEBUG') == "TRUE":
            stockJSON = "{}/{}.json".format(stockPath, stockCode)
            stockBasic.to_json(stockJSON)

if __name__ == "__main__":
    UpDataAll()


