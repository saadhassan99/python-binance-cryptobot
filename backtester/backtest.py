import asyncio
import uuid
from historical.historical_data import HistoricalData
from strategy.simple import Simple
from strategy.execute_strategy import ExecuteStrategy
from colorama import Fore, init


class Backtest:
    def __init__(self, ticker, interval, start, end):
        # self.symbol = symbol
        # self.interval = interval
        self.start = start
        # self.end = end
        self.historical_data = HistoricalData(ticker=ticker,
                                              interval=interval,
                                              start=start,
                                              end=end)
        self.strategy = None

    async def run(self):
        init(autoreset=True)

        try:
            data = await self.historical_data.getData()

            # we are using Simple as our trading strategy and we pass our buy and
            # sell signal in there, which at the moment should only print BUY SIGNAL
            self.strategy = Simple(buy_signal=self.on_buy_signal,
                                   sell_signal=self.on_sell_signal)

            # now we need to apply this strategy to our historical data
            for i in range(len(data)):
                candlestick = data[i]
                candlesticks = data[0: i + 1]
                await self.strategy.execute(candlesticks, candlestick.startTime)

            positions = self.strategy.getPositions()

            # print the total of all trades
            total = 0

            for p in positions:
                total += p.profit()
                p.print_trade()

            if total > 0:
                profit = "Profit: " + (Fore.GREEN + '$' + str(total))
                print(f"Total: {profit}")
            else:
                loss = "Loss: " + (Fore.RED + "$" + str(total))
                print(f"Total: {loss}")

        except Exception as e:
            print("Error : " + str(e))

    async def on_buy_signal(self, price, time):
        print("BUY SIGNAL")
        await self.strategy.buy(price=price,
                                quantity=1.0,
                                time=time,
                                order_id=uuid.uuid4())

    async def on_sell_signal(self, price, quantity, position, time):
        print("SELL SIGNAL")
        await self.strategy.sell(price=price,
                                 quantity=quantity,
                                 time=time,
                                 order_id=position.order_id)
