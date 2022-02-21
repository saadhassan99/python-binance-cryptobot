import uuid
from historical.historical_data import HistoricalData
from strategy.execute_strategy import ExecuteStrategy


class Backtest:
    def __init__(self, ticker, interval, start, end):
        # self.symbol = symbol
        # self.interval = interval
        # self.start = start
        # self.end = end
        self.historical_data = HistoricalData(ticker=ticker,
                                              interval=interval,
                                              start=start,
                                              end=end)

    async def run(self):
        try:
            data = await self.historical_data.getData()

        except Exception as e:
            print("Error : " + str(e))

    # async def on_buy_signal(self, price, time):
    #     # make a random UUID
    #     order_id = uuid.uuid4()
    #     exec_strategy = ExecuteStrategy()
    #     await exec_strategy.buy(price=price,
    #                             quantity=1.0,
    #                             time=time,
    #                             order_id=order_id)
    #
    # async def on_sell_signal(self, price, quatity, position, time):
    #     exec_strategy = ExecuteStrategy()
    #     await exec_strategy.sell(price=price,
    #                              quantity=quatity,
    #                              time=time,
    #                              order_id=position.order_id)