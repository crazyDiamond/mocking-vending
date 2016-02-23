#Write a test for input_coin to make sure add_coins is not called when an invalid coin is entered
#Write a test for input_coin to make sure add_coins is called when a valid coin is entered
#Write a test for input_coin to make sure t

#Refactor


import mock
import unittest
from nose import tools as nt
from vendingMachine import VendingMachine

class VendingMachineTest(unittest.TestCase):
    def setUp(self):
        self.vm = VendingMachine()

    @mock.patch('vendingMachine.VendingMachine.add_coins')
    def test_add_coins_should_not_be_called_when_coin_is_invalid(self, add_coins_):
        self.vm.valid_coins = {'a': 1, 'b': 2}

        self.vm.input_coin('c')

        assert not add_coins_.called

    @mock.patch('vendingMachine.VendingMachine.add_coins')
    def test_add_coins_should_be_called_when_coin_is_valid(self, add_coins_):
        self.vm.valid_coins = {'a': 1, 'b': 2}

        self.vm.input_coin('a')

        assert add_coins_.called

    @mock.patch('vendingMachine.VendingMachine.add_coins')
    def test_add_coins_should_be_able_to_handle_empty_string(self, add_coins_):
        self.vm.valid_coins = {'a': 1, 'b': 2}

        self.vm.input_coin('')

        assert not add_coins_.called



