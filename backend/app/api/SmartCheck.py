import os
import json

from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
from hexbytes.main import HexBytes

class SmartCheck():
    def __init__(self, contractList, network, tx_hash):
        compiled_sol = os.path.join('./build', contractList['SmartCheck'][2:].replace('.sol', '.json'))
        with open(compiled_sol, 'r') as f:
            contract_interface = json.load(f)

        # web3.py instance
        w3 = Web3(Web3.HTTPProvider(network))

        # Get tx receipt to get contract address
        tx_Hash = HexBytes(tx_hash)
        tx_receipt = w3.eth.getTransactionReceipt(tx_Hash)
        contract_address = tx_receipt['contractAddress']

        # Contract instance in concise mode
        abi = contract_interface['abi']
        contract_instance = w3.eth.contract(address=contract_address, abi=abi, ContractFactoryClass=ConciseContract)

        self.w3 = w3
        self.contract_instance = contract_instance

    def _createStudent(self, studId, age, fName, lName):
        self.contract_instance.createStudent(studId, age, fName, lName, transact={'from': self.w3.eth.accounts[0]})

    def _getParticularStudent(self, studId):
        _fName, _lName, _age, _attendanceValue = self.contract_instance.getParticularStudent(studId)
        return {
            "fName": _fName.decode('utf-8'),
            "lName": _lName.decode('utf-8'),
            "age": _age,
            "attendanceValue": _attendanceValue,
        }

    def _getStudents(self):
        return { "studIdList": self.contract_instance.getStudents() }