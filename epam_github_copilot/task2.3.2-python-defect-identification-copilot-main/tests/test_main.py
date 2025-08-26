import unittest

from booking_system.main import calculate_bill


class TestHotel(unittest.TestCase):

    def test1(self):
        room_number = 102  # Room with a pet (4kg)
        days_stayed = 5
        bill = calculate_bill(room_number, days_stayed)

        self.assertEqual(555.5, bill.total_amount)
        self.assertEqual(505.0, bill.breakdown.get("Room Charge"))
        self.assertEqual(50.5, bill.breakdown.get("Service Charge"))

    def test2(self):
        room_number = 103  # Room with a pet (12kg)
        days_stayed = 3
        bill = calculate_bill(room_number, days_stayed)

        self.assertEqual(709.5, bill.total_amount)
        self.assertEqual(645.0, bill.breakdown.get("Room Charge"))
        self.assertEqual(64.5, bill.breakdown.get("Service Charge"))

    def test3(self):
        non_existing_room_number = 999
        days_stayed = 5

        with self.assertRaises(ValueError) as context:
            calculate_bill(non_existing_room_number, days_stayed)

        self.assertTrue('Room not found.' in str(context.exception))


if __name__ == '__main__':
    unittest.main()