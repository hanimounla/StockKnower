from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

#scale the data to have simpler calculations
def get_MinMax(data,ticker):
    print ("Scaling %s stock data"%ticker)
    scaler = MinMaxScaler()
    numerical = ['Low','High','Close','Open','Med']
    data[numerical] = scaler.fit_transform(data[numerical])
    data.to_csv('Data\\%s-processed.csv'%ticker)
    print('Data processed and saved :)')
    return data

#split the data to train and test data
def split_normal(data, split_size = 0.7):
    data_size = len(data)
    split = int(data_size * split_size)
    train_data  = data[:split]
    test_data = data[split:]
    return train_data, test_data 


def split_lstm(data, prediction_time=1, test_data_size=450, unroll_length=50):
    """
        Split the data set into training and testing feature for Long Short Term Memory Model
        :param stocks: whole data set containing ['Open','Close','Volume'] features
        :param prediction_time: no of days
        :param test_data_size: size of test data to be used
        :param unroll_length: how long a window should be used for train test split
        :return: X_train : training sets of feature
        :return: X_test : test sets of feature
        :return: y_train: training sets of label
        :return: y_test: test sets of label
    """
    # training data
    test_data_cut = test_data_size + unroll_length + 1

    x_train = data[0:-prediction_time - test_data_cut].values
    y_train = data[prediction_time:-test_data_cut]['Med'].values
    # test data
    x_test = data[0 - test_data_cut:-prediction_time].values
    y_test = data[prediction_time - test_data_cut:]['Med'].values

    return x_train, x_test, y_train, y_test
 
def unroll(data, sequence_length=24):
    """
    use different windows for testing and training to stop from leak of information in the data
    :param data: data set to be used for unrolling
    :param sequence_length: window length
    :return: data sets with different window.
    """
    result = []
    for index in range(len(data) - sequence_length):
        result.append(data[index: index + sequence_length])
    return np.asarray(result)   

    

