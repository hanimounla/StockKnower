import pandas as pd
import datetime as dt
import urllib.request, json
import os

#my api_key, You can get yours from alphavantage
api_key = '3GL2O8TQS330GIZR'
# JSON file with all the stock market data for ticker from the last 20 years
url_string = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=%s&outputsize=full&apikey=%s"%(ticker,api_key)
#nice date format
today_date = dt.datetime.now().strftime("%Y.%m.%d")

# Save data to this file
file_to_save = 'Data\\%s.csv'%ticker


if not os.path.exists(file_to_save):
    with urllib.request.urlopen(url_string) as url:
        data = json.loads(url.read().decode())
        # extract stock market data
        data = data['Time Series (Daily)']
        df = pd.DataFrame(columns=['Date','Low','High','Close','Open'])
        for k,v in data.items():
            date = dt.datetime.strptime(k, '%Y-%m-%d')
            data_row = [date.date(),float(v['3. low']),float(v['2. high']),
                        float(v['4. close']),float(v['1. open'])]
            df.loc[-1,:] = data_row
            df.index += 1
#    df = df.sort_values('Date')    
    df.to_csv(file_to_save)
    print('Data saved to : %s'%file_to_save)    

# If the data is already there, just load it from the CSV
else:
    print('File already exists. Loading data from CSV')
    df = pd.read_csv(file_to_save)