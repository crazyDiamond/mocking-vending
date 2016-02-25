import mock
import unittest
from nose import tools as nt
from vending_machine import VendingMachine
from led import LED


class VendingMachineTest(unittest.TestCase):

    def setUp(self):
        self.vm_green_light_ = mock.MagicMock(spec=LED, autospec=True)

        self.vm = VendingMachine(self.vm_green_light_)

    @mock.patch('vendingMachine.VendingMachine.get_coins_value')
    def test_can_purchase_must_turn_green_light_when_purchase_is_valid(self, get_coins_value_):
        blink = mock.MagicMock(spec=LED.blink)
        self.vm_green_light_.blink = blink

        get_coins_value_.return_value = 1.00

        can_purchase = self.vm.can_purchase('apple')

        assert blink.called
        nt.assert_true(can_purchase)

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
