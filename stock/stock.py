#处理一个股票的操作

#TODO 完成基本数据下载、更新


class stockData(object):
    '''处理股票数据的类'''

    #股票代码
    def __init__(self, code):
        self.code = code
        #TODO 加载自己的数据目录配置文件，根据配置文件决定是否更新基本信息、当日交易数据