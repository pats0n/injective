#!/usr/bin/bash

CHAIN_ID=injective-1

NODE_ADDR=${1:-"https://k8s.global.mainnet.tm.injective.network:443"}

MARKET_ID=0xcf18525b53e54ad7d27477426ade06d69d8d56d2f3bf35fe5ce2ad9eb97c2fbc

injectived query exchange derivative-market  $MARKET_ID --chain-id $CHAIN_ID --node=$NODE_ADDR


