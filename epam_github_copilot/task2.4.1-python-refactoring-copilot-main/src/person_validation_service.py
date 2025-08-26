import re

from .contact import Contact


class ValidationService:

    EMAIL_PATTERN = r'^(([^<>()\\[\\]\\\\.,;:\\s@"]+(\\.[^<>()\\[\\]\\\\.,;:\\s@"]+)*)|(".+"))@((\\[[0-9]{1,3}' \
                    r'\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}])|(([a-zA-Z\\-0-9]+\\.)+[a-zA-Z]{2,}))$'

    def is_valid_email(self, email):
        return email and re.match(self.EMAIL_PATTERN, email)

    def validate_emails(self, person):
        for contact in person.contacts:
            if contact.type == Contact.EMAIL_CONTACT_TYPE and self.is_valid_email(contact.contact):
                return contact

    def validate_person(self, person):
        for contact in person.contacts:
            self.validate_contact(contact)

    def validate_contact(self, contact):
        if contact.type == Contact.EMAIL_CONTACT_TYPE:
            self.validate_email(contact.contact)

    def validate_email(self, email):
        if not self.is_valid_email(email):
            raise ValueError('Email field is empty or invalid')
