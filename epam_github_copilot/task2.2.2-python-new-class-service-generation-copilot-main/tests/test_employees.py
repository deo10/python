
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from employee_factory_project.employees import FullTimeEmployee, PartTimeEmployee, TemporaryEmployee, ContractorEmployee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        """
        setUp method called before each test,
        creating instances of each type of Employee with its respective default hourly rate.
        """
        self.full_time_employee = FullTimeEmployee()
        self.part_time_employee = PartTimeEmployee()
        self.temporary_employee = TemporaryEmployee()
        self.contractor_employee = ContractorEmployee()

        self.employees = [self.full_time_employee, self.part_time_employee,
                          self.temporary_employee, self.contractor_employee]

    def test_hourly_rates_exist(self):
        """Test that hour rates are set correctly based on EmployeeType."""

        for employee in self.employees:
            self.assertIsNotNone(employee.hourly_rate)

    def test_employee_as_string(self):
        """Test str(Employee) returns correctly formatted string."""

        for employee in self.employees:
            self.assertEqual(
                str(employee),
                f"Employee type: {employee.__class__.__name__}, Hourly Rate: {employee.hourly_rate}"
            )
