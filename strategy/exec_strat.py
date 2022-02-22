from models.trade import Trade
from models.position import Position


class ExecStrat:

    def __init__(self, buy_signal, sell_signal):
        self.buy_signal = buy_signal
        self.sell_signal = sell_signal
        self.filled_orders = {}

    # positionOpened
    async def buy(self, price, quantity, time, order_id):
        trade = Trade(price, quantity, time)
        position = Position(trade, order_id)
        self.filled_orders[order_id] = position

    # positionClosed
    async def sell(self, price, quantity, time, order_id):
        trade = Trade(price, quantity, time)
        position = self.filled_orders[order_id]

        if position:
            position.close(trade)

    def getPositions(self):
        return list(self.filled_orders.values())

    def openPositions(self):
        return list(filter(lambda x: x.state == 'open', self.filled_orders.values()))
