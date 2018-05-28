from unittest import TestCase
from rent import Rent 

class TestRentMethods(TestCase):

    def setUp(self):
        self.rent = Rent()
    
    def tearDown(self):
        self.rent = None

    def test_create_rent(self):
        self.assertIsInstance(self.rent, Rent)

    def test_rent_none(self):
        # when not rent at all
        self.assertEqual(self.rent.total_amount, 0)

    def test_rent_each_kind(self):
        # one of each kind must be $85
        self.assertEqual(self.rent.by_hour(1).by_day(1).by_week(1).total_amount, 85)

    def test_rent_by_one_hour(self):
        # one hour (default) rent must be $5
        self.assertEqual(self.rent.by_hour().total_amount, 5)

    def test_rent_by_six_hours(self):
        # six hour rent must be $30
        self.assertEqual(self.rent.by_hour(6).total_amount, 30)
    
    def test_rent_by_one_day(self):
        # one day (default) rent must be $20
        self.assertEqual(self.rent.by_day().total_amount, 20)

    def test_rent_by_two_days(self):
        # two day rent must be $40
        self.assertEqual(self.rent.by_day(2).total_amount, 40)
    
    def test_rent_by_week(self):
        # one week (default) rent must be $60
        self.assertEqual(self.rent.by_week().total_amount, 60)

    def test_rent_by_two_weeks(self):
        # two week rent must be $120
        self.assertEqual(self.rent.by_week(2).total_amount, 120)
    
    def test_rent_with_family_promotion(self):
        # this rent must be $10 + $40 + $60 
        rent = self.rent.by_hour(2).by_day(2).by_week(1)
        
        # without the promotion total value are 110
        self.assertEqual(rent.total_amount, 110)

        # appling promotion
        rent.apply_family_promotion()
        
        # total value must be 110 - 33 (30%)
        self.assertEqual(rent.total_amount, 77)

    def test_raise_noapply_promotion(self):
        # check that rent.apply_family_promotion fails when the promotional condition not apply
        with self.assertRaises(ValueError):
            pass
            # no rent at all
            self.rent.apply_family_promotion()

            # less of 3 rents
            self.rent.by_hour().by_day().apply_family_promotion()
            
            # more of 5 rents
            self.rent.by_week().by_hour().by_day().by_week().apply_family_promotion()

if __name__ == '__main__':
    unittest.main()



