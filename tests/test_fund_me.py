from brownie import network, accounts, exceptions
from scripts.helpfull_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIORNMENTS
from scripts.deploy import deploy_fund_me
import pytest

def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee()
    tx = fund_me.fund({"from": account,"value": entrance_fee + 5 * 10**17})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee + 5 * 10**17
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0

def test_can_withdraw_with_owner_accounts():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIORNMENTS:
        pytest.skip("This test is only for local enviornments")
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})
