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

def getStockPath(stockCode = ""):
    "股票代码用数字表示股票的不同含义。"\
    "沪市票买卖的代码是以600或601打头，" \
    "如：运盛实业，股票代码是600767，中国国航(7.72,0.32,4.32%)是601111。" \
    "B股买卖的代码是以900打头，" \
    "如：上电B股(0.448,0.00,0.90%)，代码是900901。"\
    "深市A股票买卖的代码是以000打头，" \
    "如：顺鑫农业(10.66,-0.05,-0.47%)，股票代码是000860。" \
    "B股买卖的代码是以200打头，" \
    "如：深中冠B(4.04,-0.03,-0.74%)股，代码是200018。" \
    "沪市新股申购的代码是以730打头。" \
    "如：中信证券(40.89,-0.88,-2.11%)申购的代码是730030。" \
    "深市新股申购的代码与深市股票买卖代码一样，" \
    "如：中信证券在深市市值配售代码是003030。" \
    "配股代码，沪市以700打头，深市以080打头。" \
    "如：运盛实业配股代码是700767。深市草原兴发配股代码是080780。" \
    "中小板股票代码以002打头，" \
    "如：东华合创(33.06,0.27,0.82%)代码是002065。" \
    "股票代码除了区分各种股票，也有其潜在的意义，" \
    "比如600***是大盘股，6006**是最早上市的股票，" \
    "有时候，一个公司的股票代码跟车牌号差不多，能够显示出这个公司的实力以及知名度，" \
    "比如000088盐田港，000888峨眉山。" \
    "在上海证券交易所上市的证券，根据上交所'证券编码实施方案'，" \
    "采用6位数编制方法，前3位数为区别证券品种，" \
    "具体见下表所列：" \
    "001×××国债现货；" \
    "110×××120×××企业债券；" \
    "129×××100×××可转换债券；" \
    "201×××国债回购；" \
    "310×××国债期货；" \
    "500×××550×××基金；" \
    "600×××A股；" \
    "700×××配股；" \
    "710×××转配股；" \
    "701×××转配股再配股；" \
    "711×××转配股再转配股；" \
    "720×××红利；" \
    "730×××新股申购；" \
    "735×××新基金申购；" \
    "737×××新股配售；" \
    "900×××B股。"

    stockCode= stockCode.strip()

    if stockCode == "":
        return "data"

    #上海A
    if stockCode.startswith("600"):
        return "data\SHA\\" + stockCode
    #上海A
    if stockCode.startswith("601"):
        return "data\SHA\\" + stockCode
    #上海B
    if stockCode.startswith("900"):
        return "data\SHB\\" + stockCode

    #深圳A
    if stockCode.startswith("000"):
        return "data\SZA\\" + stockCode
    #深圳B
    if stockCode.startswith("002"):
        return "data\SZA\\" + stockCode
    #创业板
    if stockCode.startswith("300"):
        return "data\SZCY\\" + stockCode
    #中小版
    if stockCode.startswith("200"):
        return "data\SZZX\\" + stockCode