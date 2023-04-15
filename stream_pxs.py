#!/bin/env python3

import asyncio
import logging

from pyinjective.async_client import AsyncClient  # type: ignore
from pyinjective.constant import Network  # type: ignore

import markets


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network, insecure=False)

    m = markets.Map()

    await m.main(network)

    # eth_id = m.markets["ETH/USDT PERP"]
    btc_id = m.markets["BTC/USDT PERP"]

    l = []

    # l.append(eth_id)
    l.append(btc_id)

    market_ids = l
    orderbooks = await client.stream_derivative_orderbook_snapshot(l)
    async for orderbook in orderbooks:
        print(orderbook)
        print(orderbook.operation_type)
        print(orderbook.timestamp)
        print(orderbook.market_id)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
