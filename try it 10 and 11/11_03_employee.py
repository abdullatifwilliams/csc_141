# test_employee.py

import pytest
from employee import Employee  # Import the Employee class

def test_give_default_raise():
    """Test the default raise of $5000."""
    employee = Employee('John', 'Doe', 50000)
    employee.give_raise()  # Apply the default raise
    assert employee.annual_salary == 55000, f"Expected 55000 but got {employee.annual_salary}"

def test_give_custom_raise():
    """Test a custom raise amount."""
    employee = Employee('Jane', 'Smith', 60000)
    employee.give_raise(10000)  # Apply a custom raise of $10000
    assert employee.annual_salary == 70000, f"Expected 70000 but got {employee.annual_salary}"
