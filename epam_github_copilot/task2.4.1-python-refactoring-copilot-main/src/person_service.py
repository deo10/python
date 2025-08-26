from contact import Contact
from person_email_service import EmailService
from person_validation_service import ValidationService


class PersonService:

    persons = []

    def __init__(self):
        self.email_service = EmailService()
        self.validation_service = ValidationService()

    def store(self, person):
        self.persons.append(person)
        self.email_service.greet_person(person)

    def find_person_by_email(self, email):
        for person in self.persons:
            for contact in person.contacts:
                if contact.type == Contact.EMAIL_CONTACT_TYPE and contact.contact == email:
                    return contact
