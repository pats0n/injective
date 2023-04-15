#!/bin/env python3

import asyncio
import logging

from pyinjective.async_client import AsyncClient  # type: ignore
from pyinjective.constant import Network  # type: ignore

import markets


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.mainnet()
    client = AsyncClient(network, insecure=False)

    m = markets.Map()

    await m.main()

    eth_id = m.markets["ETH/USDT PERP"]
    btc_id = m.markets["BTC/USDT PERP"]

    market_ids = [eth_id]
    orderbooks = await client.stream_derivative_orderbook_snapshot(
        market_ids=[eth_id,btc_id]
    )
    async for orderbook in orderbooks:
        # print(orderbook)
        print(orderbook.operation_type)
        print(orderbook.timestamp)
        print(orderbook.market_id)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
