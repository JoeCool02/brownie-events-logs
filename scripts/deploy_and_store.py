from distutils.command.config import config
from scripts.helpful_scripts import get_account
from brownie import SimpleStorage, config, network


def deploy():
    account = get_account()
    simple_storage = SimpleStorage.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    store_tx = simple_storage.store(1, {"from": account})
    store_tx.wait(1)
    print(store_tx.events[0]["newNumber"])


def main():
    deploy()


# {"from": account}
