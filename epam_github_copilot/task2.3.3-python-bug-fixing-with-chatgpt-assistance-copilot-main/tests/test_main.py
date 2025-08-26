import unittest
from unittest.mock import patch

from booking_system.main import HotelBookingService, Room


class TestHotelBookingService(unittest.TestCase):
    @patch('random.choice', return_value='single')
    def setUp(self, mock_random_choice):
        self.hotel = HotelBookingService()
        # Make all rooms unreserved
        for room in self.hotel.rooms:
            room.reserved = False

    def test1(self):
        result = self.hotel.book_room('single', 'John Doe')
        self.assertIsNotNone(result)
        self.assertTrue(result.reserved)
        self.assertEqual(result.guest_name, 'John Doe')

    def test2(self):
        # Make all rooms reserved
        for room in self.hotel.rooms:
            room.reserved = True

        result = self.hotel.book_room('suite', 'John Doe')
        self.assertIsNone(result)

    def test3(self):
        result = self.hotel.book_room('quadruple', 'John Doe')
        self.assertIsNone(result)

    def test4(self):
        booked_room = self.hotel.book_room('single', 'John Doe')
        cancelled_room = self.hotel.cancel_booking(booked_room.r_number)
        self.assertIsNone(cancelled_room.guest_name)
        self.assertFalse(cancelled_room.reserved)

    def test5(self):
        # At the setup, all rooms are made available
        available_rooms = self.hotel.list_available_rooms()
        self.assertEqual(len(available_rooms), len(self.hotel.rooms))

    def test6(self):
        room_number = 101
        room = self.hotel.get_room_details(room_number)
        self.assertEqual(room.r_number, room_number)

    def test7(self):
        guests = ["John Doe", "Alex Smith", "Sally Johnson"]
        for i, guest_name in enumerate(guests):
            self.hotel.rooms[i].reserved = True
            self.hotel.rooms[i].guest_name = guest_name
        result = self.hotel.list_guests()
        self.assertEqual(result, guests)

    def test8(self):
        room_number = 101
        new_type = 'suite'
        changed = self.hotel.change_room_type(room_number, new_type)
        room = self.hotel.get_room_details(room_number)
        self.assertTrue(changed)
        self.assertEqual(room.r_type, new_type)

    def test9(self):
        total_single_rooms = self.hotel.get_total_rooms_by_type('single')
        self.assertEqual(total_single_rooms, len(self.hotel.rooms))

    def test10(self):
        self.hotel.book_room('single', 'John Doe')
        reserved_single_rooms = self.hotel.get_reserved_rooms_by_type('single')
        self.assertEqual(reserved_single_rooms, 1)


if __name__ == '__main__':
    unittest.main()
