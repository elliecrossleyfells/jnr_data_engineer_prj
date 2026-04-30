import yfinance as yf

# define the function to call to the API and get stock data
def get_apple_stock():
    apple = yf.Ticker("AAPL") # AAPL = Apple’s stock symbol. Ticker creates an object representing stock 
    data = apple.history(start = "2026-04-01", end = "2026-04-29") #get past stock prices in April (can also use period = "xd") 
    return data