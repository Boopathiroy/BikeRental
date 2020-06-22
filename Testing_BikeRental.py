
import unittest
from datetime import datetime, timedelta
from BikeRental import Bikerental,Customer

class BikeRentalTest(unittest.TestCase):
    def test_rental_displaystock(self):
        shop = Bikerental()
        shop1 = Bikerental(10)
        self.assertEqual(shop.display_stock(),0)
        self.assertEqual(shop1.display_stock(),10)

    def test_returnonHourlyBasis(self):
        shop = Bikerental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rent_On_Hourly_Basis(10).hour,hour)

    def test_returnOnDailybasis(self):
        shop = Bikerental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rent_on_daily_basis(10).hour,hour)

    def test_returnOnweeklyBasis(self):
        shop = Bikerental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rent_on_weely_basis(2).hour,hour)

    def test_returnBike_for_invalid_no_ofBikes(self):
        shop = Bikerental(2)
        cus = Customer()
        cus.rental_basis = 3
        cus.rental_time = datetime.now()
        cus.no_of_bikes = 4
        request = cus.return_bike()
        self.assertEqual(shop.returnBike(request),0)


    def test_returnBike(self):
        shop = Bikerental(10)
        cus1 = Customer()
        cus1.rental_time = datetime.now() + timedelta(hours=-4)
        cus1.rental_basis =1
        cus1.no_of_bikes = 1
        request = cus1.return_bike()
        self.assertEqual(shop.returnBike(request),20)
class CustomerTest(unittest.TestCase):

    def test_return_bike(self):
        customer = Customer()

        now = datetime.now()
        customer.rental_time = now
        customer.rental_basis =1
        customer.no_of_bikes = 4
        self.assertEqual(customer.return_bike(),(now,1,4))

if __name__ == '__main__':
    unittest.main()
