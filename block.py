#! /bin/env python3

import requests
import asyncio
import logging


async def main() -> None:
    block_height = "9858070"
    lcd = "https://k8s.testnet.lcd.injective.network/injective/exchange/v1beta1/derivative/orderbook/0x2e94326a421c3f66c15a3b663c7b1ab7fb6a5298b3a57759ecf07f0036793fc9"
    lcd_request = requests.get(
        lcd,
        headers={
            "Content-Type": "application/json",
            "x-cosmos-block-height": "{}".format(block_height),
        },
    ).json()
    print(lcd_request)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
