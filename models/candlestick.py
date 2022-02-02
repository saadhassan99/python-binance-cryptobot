class Candlestick:
    def __init__(self, open1, close, high, low, interval, volume):
        self.open1 = float(open1)   # open is reserved keyword
        self.close = float(close)
        self.high = float(high)
        self.low = float(low)
        self.interval = interval
        self.volume = float(volume)

    def average(self):
        return (self.high + self.low + self.close) / 3
