from brownie import SimpleStorage, accounts

# we want to test to see that when we deploy our smart contract, its started off w 0 in retrieve function


def test_deploy():
    # Use Arrange, Act, Assert for tests
    # Arrange (set up the pieces that need to be set up)
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert
    assert starting_value == expected


def test_updating_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    expected = 15
    store_tx = simple_storage.store(expected, {"from": account})
    # use a wait so you dont get weird brownie bug
    store_tx.wait(1)
    # Assert
    assert expected == simple_storage.retrieve()
