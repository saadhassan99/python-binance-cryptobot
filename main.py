import asyncio

from config.keys import api_configs
from config.cmd_args import args
from historical.historical_data import HistoricalData
from backtester.backtest import Backtest

API_KEY = api_configs.API_KEY
API_SECRET = api_configs.API_SECRET


async def main():
    backtest = Backtest(ticker=args.ticker,
                        interval=args.interval,
                        start=args.start,
                        end=args.end)

    await backtest.run()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
