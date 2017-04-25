
import tushare as ts
import os


def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        return False

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
    UpDataAll()

