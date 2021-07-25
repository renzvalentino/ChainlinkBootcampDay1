from brownie import PuCoin, config, accounts


def deployContract():
    account = accounts.add(config["wallets"]["from_key"]) or accounts[0]
    PuCoin.deploy(10000000, {'from': account})


def main():
    deployContract()
