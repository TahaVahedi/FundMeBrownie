from brownie import FundMe
from scripts.helpfull_scripts import get_account

def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entranseFee = fund_me.getEntranceFee()
    print(f"Entrance fee: {entranseFee}")
    fund_me.fund({"from": account,"value": entranseFee + 5 * 10**17})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})

def main():
    fund()
    withdraw()