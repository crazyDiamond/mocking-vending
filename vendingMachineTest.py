#Write a test to validate the inserted coin is in the list

import mock
import unittest
from nose import  tools as nt
from vendingMachine import VendingMachine

class VendingMachineTest(unittest.TestCase):

    @mock.patch('append()')
    def test_input_coin_valid_coin(self, append_):
        vm = VendingMachine()
        vm.valid_coins = {'a': 1, 'b': 2}

        vm.input_coin('c')

        assert not append_.called()



