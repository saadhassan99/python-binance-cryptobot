import asyncio
import json

from configurations import api_configs
from configurations.cmd_args import args
from historical.historical_data import HistoricalData

API_KEY = api_configs.API_KEY
API_SECRET = api_configs.API_SECRET


async def main():
    data = HistoricalData(ticker=args.ticker,
                          interval=args.interval,
                          start=args.start,
                          end=args.end)

    candlesticks = await data.getData()

    print(candlesticks)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
