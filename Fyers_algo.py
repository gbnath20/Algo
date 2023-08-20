import datetime
import pytz
from fyers_api import fyersModel
from Init_data import InitData

class StockAnalysis:

    def __init__(self, stock_details):
        self.fyers = fyersModel.FyersModel(token=InitData.access_token, is_async=False,client_id=InitData.client_id, log_path=InitData.log_path)
        self.stock_details = stock_details

    def convertEpochToIST(self, epochtime):
        epoch_time = epochtime

        utc_time = datetime.datetime.utcfromtimestamp(epoch_time)

        india_tz = pytz.timezone('Asia/Kolkata')
        india_time = utc_time.astimezone(india_tz)
        india_time_str = india_time.isoformat()
        date_str, time_str = india_time_str.replace("T", " ").split()
        return date_str, time_str

    def HistoryData(self):
        time_from = self.stock_details["TimeFrom"]
        time_to = self.stock_details["Timeto"]
        time_from_epoch = int(datetime.datetime.strptime(time_from, "%Y-%m-%d").timestamp())
        time_to_epoch = int(datetime.datetime.strptime(time_to, "%Y-%m-%d").timestamp())

        data = {"symbol": self.stock_details["symbol"], "resolution": "30", "date_format": "0",
                "range_from": "1622097600", "range_to": "1622097685", "cont_flag": "1"}

        print(self.fyers.history(data))

        History_data = self.fyers.history(data)

        print("\n\n\n")
        epochtime = History_data['candles'][0][0]
        date, time = self.convertEpochToIST(epochtime)
        OpenValue = History_data['candles'][0][1]
        HighestValue = History_data['candles'][0][2]
        LowestValue = History_data['candles'][0][3]
        CloseValue = History_data['candles'][0][4]
        volume = History_data['candles'][0][5]

        print("Time:", date + " " + time.replace("+05:30", ""))
        print("Open Value:", OpenValue)
        print("Highest Value:", HighestValue)
        print("Lowest Value:", LowestValue)
        print("Close Value:", CloseValue)
        print("Volume:", volume)
