import json

from brownie import (
    ERC20,
    accounts,
)
from brownie.network.gas.strategies import GasNowScalingStrategy

from . import deployment_config as config

DEPLOYER = accounts.load('0')

DEPLOYER = accounts[0]
REQUIRED_CONFIRMATIONS = 1

def _tx_params():
    return {
        "from": DEPLOYER,
        "required_confs": REQUIRED_CONFIRMATIONS,
        "gas_price": 0,
        "gas_limit": 8000000,
    }


DISTRIBUTION_AMOUNT = 10 ** 6 * 10 ** 18
INITIAL_AMOUNT_ERC20 = 10 ** 9 

def deploy_tokens(tx_params):
    print("deploy_tokens")
    DEPLOYER.deploy(ERC20, "DAI", "DAI", 18, gas_limit=8000000, gas_price=0, allow_revert=True)
    # coin_a = ERC20.deploy("DAI", "DAI", 18, tx_params)
    # coin_a._mint_for_testing(INITIAL_AMOUNT_ERC20 * 10 ** 18, tx_params)

    # return [coin_a.address]
    return ["0x0"]


def main():
    [coin_a] = deploy_tokens(_tx_params())
    
    print("coin_a deployed! (●'◡'●)")