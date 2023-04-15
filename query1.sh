#!/usr/bin/bash

CHAIN_ID=injective-1

NODE_ADDR=${1:-"https://k8s.global.mainnet.tm.injective.network:443"}

injectived query exchange derivative-markets --chain-id $CHAIN_ID --node=$NODE_ADDR


