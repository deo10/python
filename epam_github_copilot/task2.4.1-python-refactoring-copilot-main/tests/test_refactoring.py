import unittest
import inspect
from types import FunctionType
from src import person_service, person_email_service, person_validation_service


class TestSingleResponsibilityPrinciple(unittest.TestCase):

    def test_srp_in_class_person_service(self, *_):

        # define the class you want to inspect
        class_to_inspect = person_service.PersonService

        # obtain properties/data attributes of the class using vars() function
        attributes = vars(class_to_inspect)

        # count the number of properties which are not methods
        # attribute should not start with "__" and should not be callable
        fields_count = len([attr for attr in attributes if
                            not callable(getattr(class_to_inspect, attr)) and not attr.startswith("__")])

        # assert if the number of fields more than 3
        self.assertTrue(fields_count <= 3, f"Class {class_to_inspect.__name__} breaks SRP as it has more than 3 fields")

    def test_srp_in_class_person_email_service(self, *_):

        # define the class you want to inspect
        class_to_inspect = person_email_service.EmailService

        # obtain properties/data attributes of the class using vars() function
        attributes = vars(class_to_inspect)

        # count the number of properties which are not methods
        # attribute should not start with "__" and should not be callable
        fields_count = len([attr for attr in attributes if
                            not callable(getattr(class_to_inspect, attr)) and not attr.startswith("__")])

        # assert if the number of fields more than 3
        self.assertTrue(fields_count <= 3, f"Class {class_to_inspect.__name__} breaks SRP as it has more than 3 fields")

    def test_srp_in_class_person_validation_service(self, *_):

        # define the class you want to inspect
        class_to_inspect = person_validation_service.ValidationService

        # obtain properties/data attributes of the class using vars() function
        attributes = vars(class_to_inspect)

        # count the number of properties which are not methods
        # attribute should not start with "__" and should not be callable
        fields_count = len([attr for attr in attributes if
                            not callable(getattr(class_to_inspect, attr)) and not attr.startswith("__")])

        # assert if the number of fields more than 4
        self.assertTrue(fields_count <= 4, f"Class {class_to_inspect.__name__} breaks refactoring goal as it has more than 4 fields")

    def test_srp_in_methods(self, *_):

        # Check that no method in each class overlaps in functionality
        # This can be tricky and somewhat subjective, but can be achieved through
        # ensuring function names reflect what they do and several other best practices

        services = [person_service.PersonService, person_validation_service.ValidationService,
                    person_email_service.EmailService]
        for service in services:
            obj = service()
            methods = [f for f in dir(obj) if isinstance(getattr(obj, f), FunctionType)]
            self.assertLessEqual(len(methods), 1, f"More than 1 public methods found in {service.__name__}")

    # Test if needed methods present in the classes
    def test_methods_present_in_classes(self):

        self.assertTrue("is_valid_email" in dir(person_validation_service.ValidationService))
        self.assertTrue("validate_emails" in dir(person_validation_service.ValidationService))

        self.assertTrue("store" in dir(person_service.PersonService))
        self.assertTrue("find_person_by_email" in dir(person_service.PersonService))

        self.assertTrue("greet_person" in dir(person_email_service.EmailService))

    # Test if modules were created
    def test_modules_created(self):
        self.assertTrue("person_service", globals())
        self.assertIn("person_validation_service", globals())
        self.assertIn("person_email_service", globals())

    # Test if classes have been created
    def test_classes_created(self):
        self.assertIsNotNone(inspect.getmembers(person_service, predicate=inspect.isclass))
        self.assertIsNotNone(inspect.getmembers(person_validation_service, predicate=inspect.isclass))
        self.assertIsNotNone(inspect.getmembers(person_email_service, predicate=inspect.isclass))


if __name__ == '__main__':
    unittest.main()
