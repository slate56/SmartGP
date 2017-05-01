#处理一个股票的操作
import UtilsTools as ut
import tushare as ts
import pandas as pd
import os

#TODO 股票类代表一支股票

class stockObject(object):
    '''处理股票数据的类'''

    Series = None
    lastUpdateTime = None

    '''code,代码
    name,名称
    industry,所属行业
    area,地区
    pe,市盈率
    outstanding,流通股本(亿)
    totals,总股本(亿)
    totalAssets,总资产(万)
    liquidAssets,流动资产
    fixedAssets,固定资产
    reserved,公积金
    reservedPerShare,每股公积金
    esp,每股收益
    bvps,每股净资
    pb,市净率
    timeToMarket,上市日期
    undp,未分利润
    perundp, 每股未分配
    rev,收入同比(%)
    profit,利润同比(%)
    gpr,毛利率(%)
    npr,净利润率(%)
    holders,股东人数'''

    #股票代码
    def __init__(self, stockSeries, LoadFromFile = True):
        '''
        code,代码
        name,名称
        industry,所属行业
        area,地区
        pe,市盈率
        outstanding,流通股本(亿)
        totals,总股本(亿)
        totalAssets,总资产(万)
        liquidAssets,流动资产
        fixedAssets,固定资产
        reserved,公积金
        reservedPerShare,每股公积金
        esp,每股收益
        bvps,每股净资
        pb,市净率
        timeToMarket,上市日期
        undp,未分利润
        perundp, 每股未分配
        rev,收入同比(%)
        profit,利润同比(%)
        gpr,毛利率(%)
        npr,净利润率(%)
        holders,股东人数
        '''

        assert(stockSeries != None)

        self.Series = stockSeries
        self.path = ut.getStockPath(self.Series['name'])
        ut.checkdir(self.path)
        self.code = self.Series['code']
        self.name = self.Series['name']
        self.stockBasic = "{}/{}.h5".format(self.path, self.code)
        self.stockConf = "{}/{}.conf".format(self.path, self.code)

        self.Series.to_hdf(self.stockFile, "basicInfo")

        try:
            f = open(self.stockConf, 'r')  # 读写文件
            lastUpdateTime = f.readline()
        finally:
            f.close()

    def isNewStock(self):
        '''通过股票名字判断是否是新股
            股票以N开头的股票是新股
            如果股票数据没有更新，返回None
        '''
        if self.Name == None: #还没有加载数据
            return None

        if self.Name.startwith("N"):
            return True
        else:
            return False

    def updateKData(self):
        '''下载历史交易数据'''
        # TODO 根据配置文件决定是否更新基本信息、当日交易数据
        #如果没有下载过数据，就从上市日期开始下载 ，否则从上次更新日期开始下载
        startDate = self.Series['timeToMarket']
        if self.lastUpdateTime != None:
            startDate = self.lastUpdateTime
