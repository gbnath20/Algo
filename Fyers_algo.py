class stockAna


data = {"symbol":"NSE:SBIN-EQ","resolution":"30","date_format":"0","range_from":"1622097600","range_to":"1622097685","cont_flag":"1"}

print(fyers.history(data))
epoch_time = epochtime

utc_time = datetime.datetime.utcfromtimestamp(epoch_time)

india_tz = pytz.timezone('Asia/Kolkata')
india_time = utc_time.astimezone(india_tz)
india_time_str = india_time.isoformat()
date_str, time_str = india_time_str.replace("T", " ").split()

History_data = fyers.history(data)


print("\n\n\n")
epochtime = History_data['candles'][0][0]
OpenValue = History_data['candles'][0][1]
HighestValue= History_data['candles'][0][2]
LowestValue = History_data['candles'][0][3]
CloseValue = History_data['candles'][0][4]
volume = History_data['candles'][0][5]

print("Time:", date_str + " " + time_str.replace("+05:30", ""))
print("Open Value:", OpenValue)
print("Highest Value:", HighestValue)
print("Lowest Value:", LowestValue)
print("Close Value:", CloseValue)
print("Volume:", volume)
