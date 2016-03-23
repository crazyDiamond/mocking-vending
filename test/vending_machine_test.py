import mock
import unittest
from nose import tools as nt
import vending_machine
from vending_machine import VendingMachine
from led import LED


# Run this test suite with Ctrl-Shift-R (OSX) or Ctrl-Shift-F10 (Other Operating Systems)
#
# Cursor in a method will run just that method.
# Cursor at class level will run the whole suite
class VendingMachineTest(unittest.TestCase):

    def setUp(self):
        self.green_light = mock.MagicMock(spec=LED, autospec=True)
        self.vm = vending_machine.VendingMachine(self.green_light)
        self.green_blink = mock.MagicMock(spec=LED.blink)
        self.vm.green_light.blink = self.green_blink

