#!/usr/bin/env python

import unittest

from src.convert import kilometers_to_miles, miles_to_kilometers,\
        years_to_minutes, minutes_to_years, f_to_c, c_to_f

class TestConvert(unittest.TestCase):

    def test_km_to_miles(self):
        actual = kilometers_to_miles(1)
        expected = 0.621 # from google
        self.assertAlmostEqual(actual, expected, delta=0.01)

    def test_miles_to_km(self):
        actual = miles_to_kilometers(1)
        expected = 1.609 # from google
        self.assertAlmostEqual(actual, expected, delta=0.01)

    def test_years_to_minutes(self):
        # Google says there are 525,600 minutes in a year
        self.assertEqual(525600, years_to_minutes(1))

    def test_minutes_to_years(self):
        self.assertEqual(1, minutes_to_years(525600))

    def test_f_to_c(self):
        self.assertAlmostEqual(100, f_to_c(212), delta=0.01)

    def test_c_to_f(self):
        self.assertAlmostEqual(212, c_to_f(100), delta=0.01)

##########################

if __name__ == '__main__':
    unittest.main()
