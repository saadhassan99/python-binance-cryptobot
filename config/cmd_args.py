import argparse

from datetime import date
from datetime import timedelta

# Get today's date
today = date.today()
# Yesterday date
yesterday = today - timedelta(days=30)

parser = argparse.ArgumentParser(description="Specify bot configurations")
parser.add_argument('-i', '--interval', metavar='', default='1d',
                    help="candlestick interval [default: \'1d\']")
parser.add_argument('-t', '--ticker', metavar='', default='BTCUSDT',
                    help='crypto ticker symbol [default: \'BTCUSDT\']')
parser.add_argument('-s', '--start', metavar='', default=yesterday.strftime("%d %b, %Y"),
                    help='start date [Format: \'1 Jan, 2022\']')
parser.add_argument('-e', '--end', metavar='', default=today.strftime("%d %b, %Y"),
                    help='end date [Format: \'1 Jan, 2022\']')
args = parser.parse_args()
