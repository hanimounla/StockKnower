#here we will predict according to the sentiment analysis and some regression machine learning algorithms
import pandas as pd



ticker = "SAP"
#load the data
file_to_read = 'Data\\%s.csv'%ticker
df = pd.read_csv(file_to_read)





