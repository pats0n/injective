#!/bin/env python3

import asyncio
import logging

from typing import Dict, Any

from pyinjective.async_client import AsyncClient  # type: ignore
from pyinjective.constant import Network  # type: ignore


class Map:
    def __init__(self) -> None:

        self.markets: Dict[str, str] = {}

    def build(self, markets: Any) -> None:

        #iterate through grpc container

        for i in range(0,len(markets.markets)):

            print(markets.markets[i].ticker, markets.markets[i].market_id)


async def main() -> None:
    # select network: local, testnet, mainnet
    # network = Network.testnet()
    network = Network.mainnet()
    client = AsyncClient(network, insecure=False)
    markets = await client.get_derivative_markets()

    m = Map()

    m.build(markets)

    # print(markets)

    # print(markets.markets[0].market_id)
    # print(markets.Header)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
