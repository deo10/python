
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from employee_factory_project.employee_factory import EmployeeFactory
from employee_factory_project.employees import FullTimeEmployee, PartTimeEmployee, TemporaryEmployee, ContractorEmployee


class TestEmployeeFactory(unittest.TestCase):
    def setUp(self):
        """
        setUp method called before each test,
        creating instance of EmployeeFactory to create employees of different types.
        """
        self.factory = EmployeeFactory()

    def test_create_employee(self):
        """Test creation of different types of employees"""

        employee_types = {
                          "fulltime": FullTimeEmployee,
                          "parttime": PartTimeEmployee,
                          "temporary": TemporaryEmployee,
                          "contractor": ContractorEmployee,
                          }

        for employee_type_str, employee_type_class in employee_types.items():
            # Creating an employee using factory
            employee = self.factory.create_employee(employee_type_str)
            # Verifying the type of employee
            self.assertIsInstance(employee, employee_type_class)

    def test_create_invalid_employee_type(self):
        """Test if creating an invalid employee type raises ValueError"""

        with self.assertRaises(ValueError):
            self.factory.create_employee("invalid_employee_type")


if __name__ == "__main__":
    unittest.main()
