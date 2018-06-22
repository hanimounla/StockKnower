from sklearn.preprocessing import MinMaxScaler
import pandas as pd

#scale the data to have simpler calculations
def process(data,ticker):
    print ("Scaling %s stock data"%ticker)
    scaler = MinMaxScaler()
    numerical = ['Low','High','Close','Open','Med']
    data[numerical] = scaler.fit_transform(data[numerical])
    data.to_csv('Data\\%s-processed.csv'%ticker)
    print('Data processed and saved :)')
    return data

#split the data to train and test data
def split(data, split_size = 0.7):
    data_size = len(data)
    split = int(data_size * split_size)
    train_data  = data[:split]
    test_data = data[split:]
    return train_data, test_data 


    

