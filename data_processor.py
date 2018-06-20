from sklearn.preprocessing import MinMaxScaler
import pandas as pd

#scale the data to have simpler calculations
def process(data,ticker):
    scaler = MinMaxScaler()
    numerical = ['Low','High','Close','Open','Med']
    data[numerical] = scaler.fit_transform(data[numerical])
    data.to_csv('Data\\%s-processed.csv'%ticker)
    print('Data processed and saved :)')
    return data

