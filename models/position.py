class Position:

    def __init__(self, trade, order_id):
        self.state = 'open'
        self.enter = trade
        self.exit = None
        self.order_id = order_id

    def close(self, trade):
        self.state = 'closed'
        self.exit = trade
