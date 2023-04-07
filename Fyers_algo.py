import datetime
import pytz
from fyers_api import fyersModel
from Init_data import InitData


class stockAnalysis:

    def __init__(self):
        self.fyers = fyersModel.FyersModel(token=InitData.access_token, is_async=False,
                                           client_id=InitData.client_id, log_path=InitData.log_path)
        self.symbol =

    def convertEpochToIST(self, epochtime):
        epoch_time = epochtime

        utc_time = datetime.datetime.utcfromtimestamp(epoch_time)

        india_tz = pytz.timezone('Asia/Kolkata')
        india_time = utc_time.astimezone(india_tz)
        india_time_str = india_time.isoformat()
        date_str, time_str = india_time_str.replace("T", " ").split()
        return date_str, time_str

    def HistoryData(self):
        data = {"symbol": "NSE:SBIN-EQ", "resolution": "30", "date_format": "1",
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
