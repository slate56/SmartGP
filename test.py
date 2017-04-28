import string

import tushare as ts
import UtilsTools as ut
import os


def DownData(df = None, stockCode = ""):
    nothing = ""

def SaveBasic(df = None, stockCode = ""):

    stockPath = ut.getStockPath(stockCode)
    ut.mkdir(stockPath)
    stockBasic = df.ix[stockCode]
    stockFile = "{}/{}.h5".format(stockPath, stockCode)
    stockBasic.to_hdf(stockFile, "basicInfo")

    if os.getenv('DEBUG') == "TRUE":
        stockJSON = "{}/{}.json".format(stockPath, stockCode)
        stockBasic.to_json(stockJSON)

def UpDataAll():
    import pandas as pd

    path = ut.getStockPath() + "all.h5"
    old_df = pd.read_hdf(path, "table")
    new_df = ts.get_stock_basics()
    

    for stockCode in new_df.index:
        DownData(new_df.ix[stockCode], stockCode)


if __name__ == "__main__":
    UpDataAll()


