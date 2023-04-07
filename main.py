from Fyers_algo import stockAnalysis
from Init_data import InitData
from fyers_api import fyersModel

if __name__ == '__main__':
    stockAnalysis = stockAnalysis()
    StockDetails = {}
    StockDetails["symbol"] = "TCS-EQ"
    StockDetails["TimeFrom"] = "2022-01-01"
    StockDetails["Timeto"] = "2022-10-01"
    stockAnalysis.__init__(StockDetails)
    stockAnalysis.HistoryData()
