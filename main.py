#our main python file, we will insert the stock ticker and will get some feedback about it from 
#Price_predection.py and Sentiment.py
import data_grapper as grapper
import data_processor as processor
import price_predictor as predictor
import visualizer as vizer
import sentiment_analyzer as s_analyzer


ticker = 'SAP'

data = grapper.grap_stock_data(ticker)
data_processed = processor.process(data,ticker)


#we've noticed that the graph is the same 
vizer.basic_plot(data, '%s original'%ticker)
vizer.basic_plot(data_processed, '%s processed'%ticker)

#try to predict the behaviour of the stock for the next week
next_week_data = predictor.predict(data_processed,ticker)

