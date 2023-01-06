from brownie import Strategy, accounts, config, network, project, web3
from eth_utils import is_checksum_address
import click


def main():
    strategist = accounts.load("strategist")
    click.echo(
        f"You are using: 'dev' [{strategist.address}] with balance {strategist.balance()}"
    )

    vault = "0xdeD8B4ac5a4a1D70D633a87A22d9a7A8851bEa1b"

    strategy = Strategy.deploy(vault, "CurveTriCryptoStrategy", {"from": strategist})
