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

            ticker = markets.markets[i].ticker
            market_id = markets.markets[i].market_id

            if ticker not in self.markets:

                self.markets[ticker] = market_id

    async def main(self, network: Any = None) -> None:

        if not network:
            network = Network.testnet()
            # network = Network.mainnet()
        client = AsyncClient(network, insecure=False)
        markets = await client.get_derivative_markets()
        print(markets)
        self.build(markets)


if __name__ == "__main__":

    m = Map()
    logging.basicConfig(level=logging.INFO)
    asyncio.run(m.main())

    print(m.markets)

    eth_id = m.markets["ETH/USDT PERP"]

    print(eth_id)
