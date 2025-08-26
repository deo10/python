from typing import List, Optional, Dict


class Room:

    def __init__(self, room_number: int, room_type: str, reserved: bool, sea_view: bool, extras: List[str],
                 pet: Optional[Dict[str, int]]):
        self.room_number = room_number
        self.room_type = room_type
        self.reserved = reserved
        self.sea_view = sea_view
        self.extras = extras
        self.pet = pet


class Bill:

    def __init__(self, total_amount: float, breakdown: Dict[str, float]):
        self.total_amount = total_amount
        self.breakdown = breakdown


rooms = [
    Room(101, 'single', False, False, ['wifi'], None),
    Room(102, 'double', False, True, [], {'weight': 4}),
    Room(103, 'suite', False, True, ['minibar', 'wifi'], {'weight': 12}),
    # ... other rooms
]

room_rates = {
    'single': 50,
    'double': 80,
    'suite': 150
}

extras_rate = {
    'minibar': 15,
    'wifi': 5
}

# Moved the petFeeRates constant here
pet_fee_rates = {
    'under5kg': 5,
    'under10kg': 10,
    'over10kg': 15
}


def calculate_bill(room_number: int, days_stayed: int) -> Bill:
    room_details = get_room_details(room_number)

    daily_rate = room_rates[room_details.room_type]

    if room_details.sea_view:
        daily_rate += daily_rate * 0.2  # 20% surcharge for sea view

    for extra in room_details.extras:
        daily_rate += extras_rate[extra]

    if room_details.pet:
        pet_weight = room_details.pet.get('weight', 0)
        if pet_weight <= 5:
            daily_rate += pet_fee_rates['under5kg']
        elif pet_weight <= 10:
            daily_rate += pet_fee_rates['under10kg']
        else:
            daily_rate += pet_fee_rates['over10kg']

    total_amount = daily_rate * days_stayed

    service_charge = total_amount * 0.1  # 10% service charge

    final_amount = total_amount + service_charge

    return Bill(final_amount, {
        'Room Charge': total_amount,
        'Service Charge': service_charge
    })


def get_room_details(room_number: int) -> Room:
    room = next((r for r in rooms if r.room_number == room_number), None)

    if not room:
        raise ValueError('Room not found.')

    return room
