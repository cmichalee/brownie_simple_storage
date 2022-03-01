from brownie import accounts, config, SimpleStorage, network
import os

# there are threew ways to work with accounts in brownie
def deploy_simple_storage():
    # account = accounts[0]
    # above account usage is for local ganache account, below are other ways to use accounts
    # account = accounts.load("freecodecamp-account")
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # account = accounts.add(config["wallets"]["from_key"])

    account = get_account()

    # every time you deploy a contract, you need a from
    # brownie is smart enough to know if it is a call or transaction
    simple_storage = SimpleStorage.deploy({"from": account})
    # since retrieve is a call, you do not need to add a "from"
    stored_value = simple_storage.retrieve()
    print(stored_value)
    # store is a transaction, so we need a "from"
    transaction = simple_storage.store(15, {"from": account})
    # how many blocks you want to wait
    transaction.wait(1)
    # check the new value
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


# adding this function to check if we are using a testnet or devnet and use accounts accordingly
def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
