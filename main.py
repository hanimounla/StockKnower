#our main python file, we will insert the stock ticker and will get some feedback about it from 
#Price_predection.py and Sentiment.py
import data_grabber as grabber
import data_processor as processor
import visualizer as vizer
import time
import models


ticker = 'SAP'

data = grabber.grab_stock_data(ticker)
data_processed = processor.get_MinMax(data,ticker) #make the data range from 0 to 1 


#we will noticed that the graphs are the same 
#vizer.basic_plot(data, '%s original'%ticker)
vizer.basic_plot(data_processed, '%s processed'%ticker)


#Creating the machine learning model
x_train, x_test, y_train, y_test = processor.split_lstm(data_processed)
# Set up hyperparameters
batch_size = 512
epochs = 20

unroll_length = 50
x_train = processor.unroll(x_train, unroll_length)
x_test = processor.unroll(x_test, unroll_length)
y_train = y_train[-x_train.shape[0]:]
y_test = y_test[-x_test.shape[0]:]

print("x_train", x_train.shape)
print("y_train", y_train.shape)
print("x_test", x_test.shape)
print("y_test", y_test.shape)

# build improved lstm model
model = models.build_LSTM_model(x_train.shape[-1],output_dim = unroll_length, return_sequences=True)

start = time.time()
#final_model.compile(loss='mean_squared_error', optimizer='adam')
model.compile(loss='mean_squared_error', optimizer='adam')
print('compilation time : ', time.time() - start)

#training
model.fit(x_train, 
          y_train, 
          batch_size=batch_size,
          epochs=epochs,
          verbose=2,
          validation_split=0.05
         )

# Generate predictions 
predictions = model.predict(x_test, batch_size=batch_size)


