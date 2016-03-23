import mock
import unittest
from nose import tools as nt
import vending_machine
from vending_machine import VendingMachine
from led import LED


class VendingMachineTest(unittest.TestCase):


    def setUp(self):
        self.green_light = mock.MagicMock(spec=LED, autospec=True)
        self.vm = vending_machine.VendingMachine(self.green_light)
        self.green_blink = mock.MagicMock(spec=LED.blink)
        self.vm.green_light.blink = self.green_blink

    def test_can_purchase_with_orange_and_74_cents_returns_false(self):
        self.vm.get_coins_value = lambda: 0.74
        # Use this as a debugger if you have problems
        # import ipdb;ipdb.set_trace()
        assert not self.vm.can_purchase(vending_machine.ORANGE)

    def test_can_purchase_with_orange_and_75_cents_returns_true(self):
        self.vm.get_coins_value = mock.MagicMock('vending_machine.VendingMachine.get_coins_value', return_value=0.75)

        assert self.vm.can_purchase(vending_machine.ORANGE)

    @mock.patch('vending_machine.VendingMachine.get_coins_value')
    def test_cannot_purchase_orange_when_coins_value_is_64_cents_(self, get_coins_value_):
        get_coins_value_.return_value = 0.76

        assert self.vm.can_purchase(vending_machine.ORANGE)

    def test_can_purchase_with_apple_calls_green_light_blink(self):
        self.vm.can_purchase(vending_machine.APPLE)
        assert self.green_blink.called

    def test_can_purchase_with_apple_and_64_cents_does_not_call_blink(self):
        self.vm.get_coins_value = lambda: 0.64

        self.vm.can_purchase(vending_machine.APPLE)

        assert not self.green_blink.called

    def test_input_coin_with_bad_coin_does_not_call_add_coins(self):
        add_coins_mock = mock.MagicMock('vending_machine.VendingMachine.add_coins')
        self.vm.add_coins = add_coins_mock
        self.vm.valid_coins = {'a': 1, 'b': 2}

        self.vm.input_coin('c')

        assert not add_coins_mock.called
