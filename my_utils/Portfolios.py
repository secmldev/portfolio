import pandas as pd
import matplotlib.pyplot as plt


class portfolio():
    
    def __init__(self,signals,initial_capital):
        self.initial_capital = initial_capital
        self.signals = signals
        
    def create_positions(self):
        
        # Open the Long flag for first trade to buy
        is_Long=True 
        holdings=[0]  
        cash=[self.initial_capital]
        inventory=[0] 
        buying_capacity=0

        for i in range(len(self.signals)):

            if self.signals["buy_sell_signal"][i] == 1 and cash[i] > 0 and is_Long==True:
                is_Long=False
                buying_capacity =int(cash[i] /self.signals["Adj Close"][i])
                holdings.append(self.signals["Adj Close"][i] * buying_capacity)
                cash.append(cash[i] - self.signals["Adj Close"][i] * buying_capacity)
                inventory.append(buying_capacity)

            elif self.signals["buy_sell_signal"][i] == -1 and is_Long==False:
                is_Long=True
                holdings.append(0)
                cash.append(cash[i] + self.signals["Adj Close"][i] * buying_capacity)
                inventory.append(0)

            else:  
                inventory.append(inventory[i])
                holdings.append(inventory[i] * self.signals["Adj Close"][i])
                cash.append(cash[i])


        portfolio_frame = {'cash':cash, 'holdings':holdings, 'inventory':inventory }
        portfolio = pd.DataFrame(portfolio_frame)
        portfolio['total'] = portfolio['cash'] + portfolio['holdings']
        
        return portfolio
    
    
    def Plot_portfolio(self,positions):
        positions[["total","cash"]].plot(figsize = (16,4) , grid = True)
        plt.savefig('portfolio.png')
        
    
    
    