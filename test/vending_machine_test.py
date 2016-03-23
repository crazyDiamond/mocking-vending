import mock
import unittest
from nose import tools as nt
import vending_machine
from vending_machine import VendingMachine
from led import LED


class VendingMachineTest(unittest.TestCase):

    def setUp(self):
        self.vm_green_light = mock.MagicMock(spec=LED, autospec=True)

        self.vm = VendingMachine(self.vm_green_light)

    def test_add_coins_should_not_be_called_when_coin_is_invalid_using_magic_mock(self):
        add_coins = mock.MagicMock('vending_machine.VendingMachine.add_coins')

        self.vm.valid_coins = {'a': 1, 'b': 2}

        self.vm.input_coin('c')

        assert not add_coins.called

    @mock.patch('vending_machine.VendingMachine.add_coins')
    def test_add_coins_should_not_be_called_when_coin_is_invalid(self, add_coins_):
        self.vm.valid_coins = {'a': 1, 'b': 2}

        self.vm.input_coin('c')

        assert not add_coins_.called

    @mock.patch('vending_machine.VendingMachine.add_coins')
    def test_add_coins_should_be_called_when_coin_is_valid(self, add_coins_):
        self.vm.valid_coins = {'a': 1, 'b': 2}

        self.vm.input_coin('a')

        assert add_coins_.called

    @mock.patch('vending_machine.VendingMachine.add_coins')
    def test_add_coins_should_be_called_when_coin_is_valid(self, add_coins_):
        self.vm.valid_coins = {'a': 1, 'b': 2}

        self.vm.input_coin('a')

        assert add_coins_.called


    @mock.patch('vending_machine.VendingMachine.get_coins_value')
    def test_can_purchase_must_turn_green_light_when_purchase_is_valid(self, get_coins_value_):
        blink = mock.MagicMock(spec=LED.blink)
        self.vm_green_light.blink = blink

        get_coins_value_.return_value = 1.00

        can_purchase = self.vm.can_purchase('apple')

        assert blink.called
        nt.assert_true(can_purchase)




    def test_can_purchase_banana_when_coins_value_is_one_dollar(self):
        self.vm.get_coins_value = lambda: 1.0

        assert self.vm.can_purchase(vending_machine.BANANA)

    def test_cannot_purchase_banana_when_coins_value_is_99_cents(self):
        self.vm.get_coins_value = lambda: 0.99

        assert not self.vm.can_purchase(vending_machine.BANANA)

    def test_cannot_purchase_orange_when_coins_value_is_74_cents_(self):
        self.vm.get_coins_value = mock.MagicMock('get_coins_value', return_value=0.74)

        assert not self.vm.can_purchase(vending_machine.ORANGE)

    @mock.patch('vending_machine.VendingMachine.get_coins_value')
    def test_cannot_purchase_orange_when_coins_value_is_64_cents_(self, get_coins_value_):
        get_coins_value_.return_value  = 0.64

        assert not self.vm.can_purchase(vending_machine.APPLE)

    @mock.patch('vending_machine.VendingMachine.add_coins')
    def test_add_coins_should_be_able_to_handle_empty_string(self, add_coins_):
        self.vm.valid_coins = {'a': 1, 'b': 2}

        self.vm.input_coin('')

        assert not add_coins_.called
