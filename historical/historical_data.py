from binance import AsyncClient
from models.candlestick import Candlestick


# client = await AsyncClient.create(API_KEY, API_SECRET, tld='us')

class HistoricalData:
    def __init__(self, ticker, interval, start, end):
        self.ticker = ticker
        self.interval = interval
        self.start = start
        self.end = end

    async def getData(self):
        client = AsyncClient()
        responses = await client.get_historical_klines(symbol=self.ticker,
                                                       interval=self.interval,
                                                       start_str=self.start,
                                                       end_str=self.end)
        await client.close_connection()

        candlesticks = list(map(self.create_candlesticks, responses))

        return candlesticks

    def create_candlesticks(self, res):
        return Candlestick(open1=res[1],
                           close=res[4],
                           high=res[2],
                           low=res[3],
                           interval=self.interval,
                           volume=res[5])
