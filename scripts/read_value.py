# this is going to read from a contract we already deployed on rinkeby blockchain

from brownie import SimpleStorage, accounts, config


def read_contract():
    # SimpleStorage is actually just an array we can access by indexing
    # To always work with most recent deployment, use -1 index
    # Brownie knows address and ABI
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())


def main():
    read_contract()
