# Task2.2.2-python New Class-Service Generation Template

*The task description covers only the initial requirements. For training purposes, the task is similar to real-world situations, with the developer learning about specific requirements during the development process. Use the test results to examine and identify all requirements.*

In modern web development, developers often create classes and services to manage specific functionalities. With AI tools like Copilot, this process can be streamlined and made more efficient. In this task, you will be seeking assistance from ChatGPT to construct a Python class that combines methods and integrates the Factory Method design pattern:

* Employee Factory Class: Create a class named EmployeeFactory. This class will have a method called create_employee.
* Different Employee Types: The create_employee method should accept a type parameter (like "fulltime", "parttime", "temporary", "contractor"). Depending on the provided type, it should return an instance of the respective class. Each employee type class (e.g., FullTime, PartTime, etc.) should have a property hourly to store hourly rates.
* Display Method: Every employee instance should have a method say to log their type and hourly rate.