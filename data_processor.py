from sklearn.preprocessing import MinMaxScaler

#scale the data to have simpler calculations
def process(data):
    scaler = MinMaxScaler()
    numerical = ['Low','High','Close','Open','Med']
    data[numerical] = scaler.fit_transform(data[numerical])
