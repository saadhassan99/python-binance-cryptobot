from strategy.execute_strategy import ExecuteStrategy


class Simple(ExecuteStrategy):

    async def execute(self, candlesticks, time):
        length = len(candlesticks)

        # make sure we have atleast 20 candlesticks worth of data before we
        # make a decision
        if length < 20:
            return

        penultimate = candlesticks[length - 2].close
        last = candlesticks[length - 1].close
        price = last

        open_positions = self.openPositions()

        if (len(open_positions) == 0):
            if last < penultimate:
                self.buy_signal(price, time)
        else:
            if last > penultimate:
                open_positions.
