import unittest
import nose.tools as nt
import mock

from RandoriExercise import *

class TestRandoriExercise(unittest.TestCase):

    @mock.patch("RandoriExercise.Cash.calculate")
    def testCashCalculateIsMocked(self, calculate_):
        calculate_.return_value = "done"

        cash = Cash()
        calculate = cash.calculate()

        nt.assert_equals("done", calculate)

    @mock.patch("RandoriExercise.Purchase.price")
    def testPurchasePriceIsMocked(self, price_):
        price_.return_value = 3.5

        purchase = Purchase()
        price = purchase.price()

        nt.assert_equals(3.5, price)

    @mock.patch("RandoriExercise.VendingMachine.coin_drop")
    def testAddCoin(self, coin_drop_):
        coin_drop_.return_value = "No Canadian coins allowed"

        vending = VendingMachine()

        accepts = vending.coin_drop('quarter')

        nt.assert_equals(accepts, "No Canadian coins allowed")