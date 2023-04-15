#!/bin/env python3

import asyncio
import logging

from pyinjective.async_client import AsyncClient  # type: ignore
from pyinjective.constant import Network  # type: ignore


async def main() -> None:
    network = Network.mainnet()
    client = AsyncClient(network, insecure=False)
    address = "inj1f54qtx4g0w0juzmuas7ldtj7r0u2c0w5zpp2hp"
    acc = await client.get_account(address=address)
    print(acc)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
