from Fyers_algo import StockAnalysis
from Init_data import InitData
from fyers_api import fyersModel


if __name__ == '__main__':

    StockDetails = {}
    StockDetails["symbol"] = "NSE:SBIN-EQ"
    StockDetails["TimeFrom"] = "2023-01-01"
    StockDetails["Timeto"] = "2023-07-01"
    stock_analysis = StockAnalysis(StockDetails)
    stock_analysis.HistoryData()
