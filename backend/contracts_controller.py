from __future__ import print_function
import argparse

import io
import os
import json
import shutil
import web3

from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
from solc import install_solc, compile_files

# load configs from config.json
contracts_settings = './contracts_settings.json'

with open(contracts_settings, 'r') as f:
    configs = json.load(f)
    del configs['tx_hash']

class controller():
    def __init__(self, solc_version, solc_path, contractList, contractName, network, gas, contracts_settings=contracts_settings):
        self.solc_version = solc_version
        self.solc_path = solc_path
        self.contractList = contractList
        self.contractName = contractName
        self.network = network
        self.gas = gas
        self.contracts_settings = contracts_settings

    def install(self):
        # Install solc binary
        install_solc(self.solc_version)
        solc = os.path.join(os.environ['HOME'], '.py-solc', f'solc-{self.solc_version}', 'bin', 'solc')
        path = os.path.join(self.solc_path, 'solc')
        shutil.copy(solc, path)
        return f'LATEST solc_path: {path}'

    def deploy(self):
        # Compile solidity source code
        sol_files = [value for value in self.contractList.values()]
        compiled_sol = compile_files(sol_files)
        target_sol = self.contractList[self.contractName]
        contract_interface = compiled_sol['{}:{}'.format(target_sol, self.contractName)]

        with io.open(os.path.join('./build', target_sol[2:].replace('.sol', '.json')), 'w+', encoding='utf-8') as json_file:
            json.dump(contract_interface, json_file, ensure_ascii=False)

        print('CONTRACT SUCCESSFULLY COMPILED')

        # web3.py instance
        w3 = Web3(Web3.HTTPProvider(self.network))
        # Instantiate and deploy contract
        contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
        # Get transaction hash from deployed contract
        tx_hash = contract.deploy(transaction={'from': w3.eth.accounts[0], 'gas': self.gas})
        print('CONTRACT SUCCESSFULLY DEPLOYED')

        settings = {
            "solc_version": self.solc_version,
            "solc_path": self.solc_path,
            "contractList": self.contractList,
            "contractName": self.contractName,
            "network": self.network,
            "gas": self.gas,
            "tx_hash": tx_hash.hex()
        }

        with io.open(self.contracts_settings, 'w', encoding='utf-8') as json_file:
            json.dump(settings, json_file, ensure_ascii=False)

        return f'tx_hash for DEPLOYED CONTRACT: {tx_hash.hex()}'

    def option(self, operator):
        return {
            'install': lambda: self.install(),
            'deploy': lambda: self.deploy()
        }.get(operator, lambda: None)()

if __name__=="__main__":
	parser = argparse.ArgumentParser(description='This code is written for compile & deploy smart contracts')
	parser.add_argument('--option', type=str, default='install',
			choices=['install','deploy'],
			help='What operation?')
	args = parser.parse_args()
	op = args.option

	ctrl = controller(**configs)
	print(ctrl.option(op))