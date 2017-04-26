
import tushare as ts
import UtilsTools as ut




def UpDataAll():
    ERROR_ON_READ_DATA = "TRUE"

    try:
        import pandas as pd
        df = pd.read_hdf('all.h5', 'table')
        ERROR_ON_READ_DATA = "FALSE"
    except Exception as e:
        ERROR_ON_READ_DATA = "TRUE";

    if ERROR_ON_READ_DATA == "TRUE":
        df = ts.get_stock_basics()
        df.to_hdf('all.h5', 'table')

    for stockCode in df.index:
        print(stockCode)


if __name__ == "__main__":
    #UpDataAll()
    print(ut.getStockPath())

