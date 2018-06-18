#our main python file, we will insert the stock ticker and will get some feedback about it from 
#Price_predection.py and Sentiment.py
import data_grapper as grapper
import data_processor as processor
import visualizer as vizer
import sentiment_analyzer as s_analyzer


ticker = 'SAP'

processor.process(grapper.grap_stock_data(ticker),ticker)
