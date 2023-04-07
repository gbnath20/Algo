import datetime
import pytz
from fyers_api import fyersModel


class stockAnalysis:

    def __init__(self, fyers):
        print()

    def convertEpochToIST(self, epochtime):
        epoch_time = epochtime

        utc_time = datetime.datetime.utcfromtimestamp(epoch_time)

        india_tz = pytz.timezone('Asia/Kolkata')
        india_time = utc_time.astimezone(india_tz)
        india_time_str = india_time.isoformat()
        date_str, time_str = india_time_str.replace("T", " ").split()
        return date_str, time_str

    def increment(self):
        data = {"symbol": "NSE:SBIN-EQ", "resolution": "30", "date_format": "0",
                "range_from": "1622097600", "range_to": "1622097685", "cont_flag": "1"}

        print(fyers.history(data))


        History_data = fyers.history(data)

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


access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2ODA4NDkxMjUsImV4cCI6MTY4MDkxMzgwNSwibmJmIjoxNjgwODQ5MTI1LCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCa0w3amxiZWxab092cldPYjREcUxPNlJiTllMTzJ5ZVhpazFINnlBeVZPajNFQkxpOWJGNFdQQzB6VHo0RkJ2TUVPYWhVbTc3TmJPLU1DTmdHbnp0dmN4dDFZZTJDQXdvS3dmZC1oNW5VbkFIWjh1dz0iLCJkaXNwbGF5X25hbWUiOiJSQVZJQ0hBTkRSQU4gR09QSU5BVEgiLCJvbXMiOiJLMSIsImZ5X2lkIjoiWFIzNjEwMSIsImFwcFR5cGUiOjEwMCwicG9hX2ZsYWciOiJOIn0.joD1yQRcdZRCNcKlK8IevJnWqlheiAOvQRThL5QbqKk"
fyers = fyersModel.FyersModel(token=access_token, is_async=False,
                              client_id="LB65IDSEJH-100", log_path="C:\\Users\\91994\\Documents\\Algo\\")
obj = stockAnalysis(fyers)
obj.increment()
print("me")
