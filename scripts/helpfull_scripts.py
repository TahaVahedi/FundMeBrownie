from brownie import accounts, network, config, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIORNMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 400000000000


def get_account():
    if(network.show_active() in LOCAL_BLOCKCHAIN_ENVIORNMENTS):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    if len(MockV3Aggregator) <= 0:
        print("deploying Mocks...")
        MockV3Aggregator.deploy(
            DECIMALS,
            STARTING_PRICE,
            {'from': get_account()}
            )
