import matplotlib.pyplot as plt


def basic_plot(stock_data, title = "Ticker"):
    plt.plot(range(stock_data.shape[0]),(stock_data['Med']))
    plt.xticks(range(0,stock_data.shape[0],500),stock_data['Date'].loc[::500], rotation=45)
    plt.xlabel('Date',fontsize=18)
    plt.ylabel('Mid Price',fontsize=18)
    plt.title('Stock ' +  title)
    plt.show()