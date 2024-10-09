
import ccxt

class DataFetcher:
    def __init__(self):
        self.exchange = ccxt.mexc()

    def fetch_ohlcv(self, symbol, timeframe='1d', limit=1000):
        return self.exchange.fetch_ohlcv(symbol, timeframe, limit=limit)

    def get_futures_markets(self):
        markets = self.exchange.load_markets()
        return [symbol for symbol, market in markets.items() if market['future']]
