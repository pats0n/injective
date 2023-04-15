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

        for i in range(0, len(markets.markets)):

            # print(markets.markets[i].ticker, markets.markets[i].market_id)

            self.markets[markets.markets[i].ticker] = markets.markets[i].market_id

    async def main(self) -> None:
        # select network: local, testnet, mainnet
        # network = Network.testnet()
        network = Network.mainnet()
        client = AsyncClient(network, insecure=False)
        markets = await client.get_derivative_markets()

        self.build(markets)


if __name__ == "__main__":

    m = Map()
    logging.basicConfig(level=logging.INFO)
    asyncio.run(m.main())

    print(m.markets)
