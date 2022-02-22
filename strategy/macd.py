from strategy.exec_strat import ExecStrat


class MACD(ExecStrat):

    async def run(self, candlesticks, time):
        avgPrices = list(candlestick.average() for candlestick in candlesticks)



        print(avgPrices)
