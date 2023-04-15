#!/bin/env python3

import asyncio
import logging

from pyinjective.async_client import AsyncClient  # type: ignore
from pyinjective.constant import Network  # type: ignore


async def main() -> None:
    # select network: local, testnet, mainnet
    # network = Network.testnet()
    network = Network.mainnet()
    client = AsyncClient(network, insecure=False)
    market_ids = ["0x90e662193fa29a3a7e6c07be4407c94833e762d9ee82136a2cc712d6b87d7de3"]
    orderbooks = await client.stream_derivative_orderbook_snapshot(
        market_ids=market_ids
    )
    async for orderbook in orderbooks:
        print(orderbook)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
