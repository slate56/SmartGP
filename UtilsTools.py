import os

def checkdir(path):
    '''检查目录是否存在，如果不存在就创建一个'''
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("/")

    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        return False

def getStockPath(stockCode = ""):

    stockCode= stockCode.strip()

    if stockCode == "":
        return "data/"

    #上海A
    if stockCode.startswith("600"):
        return "data/SHA/" + stockCode
    if stockCode.startswith("603"):
        return "data/SHA/" + stockCode
    if stockCode.startswith("601"):
        return "data/SHA/" + stockCode

    #上海B
    if stockCode.startswith("900"):
        return "data/SHB/" + stockCode

    #深圳A
    if stockCode.startswith("000"):
        return "data/SZA/" + stockCode
    if stockCode.startswith("001"):
        return "data/SZA/" + stockCode
    #深圳B
    if stockCode.startswith("002"):
        return "data/SZA/" + stockCode
    #创业板
    if stockCode.startswith("300"):
        return "data/SZCY/" + stockCode
    #中小版
    if stockCode.startswith("200"):
        return "data/SZZX/" + stockCode

    return "data/"