from employee_factory_project.employees import FullTimeEmployee, PartTimeEmployee, TemporaryEmployee, ContractorEmployee



class EmployeeFactory:
    """Factory class for creating different types of Employees."""

    @staticmethod
    def create_employee(employee_type):
        """
        Create and return an Employee of the specified type.

        Args:
            employee_type (str): the type of the employee to create.

        Returns:
            instance of the appropriate Employee subclass.

        Raises:
            ValueError: If `employee_type` is not recognized.
        """
        employee_type = employee_type.lower()
        if employee_type == "fulltime":
            return FullTimeEmployee()
        elif employee_type == "parttime":
            return PartTimeEmployee()
        elif employee_type == "temporary":
            return TemporaryEmployee()
        elif employee_type == "contractor":
            return ContractorEmployee()
        else:
            raise ValueError(f"Unknown employee type: {employee_type}")


if __name__ == '__main__':
    # Test the code
    factory = EmployeeFactory()
    for emp_type in ["fulltime", "parttime", "temporary", "contractor"]:
        employee = factory.create_employee(emp_type)
        employee.say()
    try:
        employee = factory.create_employee("unknown")
        employee.say()
    except ValueError as e:
        print(e)
