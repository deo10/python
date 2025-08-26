


class Employee:
    """Abstract base class for Employee."""

    def __init__(self, hourly_rate):
        self.hourly_rate = hourly_rate

    def __str__(self):
        return f"Employee type: {self.__class__.__name__}, Hourly Rate: {self.hourly_rate}"

    def say(self):
        print(str(self))

class FullTimeEmployee(Employee):
    def __init__(self):
        super().__init__(hourly_rate=40)

class PartTimeEmployee(Employee):
    def __init__(self):
        super().__init__(hourly_rate=25)

class TemporaryEmployee(Employee):
    def __init__(self):
        super().__init__(hourly_rate=20)

class ContractorEmployee(Employee):
    def __init__(self):
        super().__init__(hourly_rate=30)
