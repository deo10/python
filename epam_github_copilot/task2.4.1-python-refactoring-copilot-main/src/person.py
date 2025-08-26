from address import Address
from contact import Contact
from phone import Phone


class Person:
    
    def __init__(self, first_name, last_name, birthday, addresses, phones, contacts):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.addresses = [
            Address(
                address.type,
                address.address1,
                address.address2,
                address.zip,
                address.country,
            )
            for address in addresses
        ]
        self.phones = [
            Phone(
                phone.type,
                phone.number,
            )
            for phone in phones
        ]
        self.contacts = [
            Contact(
                contact.type,
                contact.contact,
            )
            for contact in contacts
        ]
