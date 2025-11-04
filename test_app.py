#!/usr/bin/env python3
"""
Test suite for the simple calculator app.
These tests can be run with pytest or unittest to validate the application.
"""

import unittest
import pytest
from app import add, subtract, multiply, divide, get_operation_result


class TestCalculatorFunctions(unittest.TestCase):
    """Test cases for individual calculator functions."""
    
    def test_add(self):
        """Test addition function."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-5, -3), -8)
    
    def test_subtract(self):
        """Test subtraction function."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, 1), 0)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-3, -1), -2)
    
    def test_multiply(self):
        """Test multiplication function."""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(0, 10), 0)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(-3, -4), 12)
    
    def test_divide(self):
        """Test division function."""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(0, 5), 0)
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            divide(10, 0)
        
        with self.assertRaises(ValueError):
            divide(-5, 0)


class TestOperationResult(unittest.TestCase):
    """Test cases for the operation dispatcher function."""
    
    def test_valid_operations(self):
        """Test all valid operations through get_operation_result."""
        self.assertEqual(get_operation_result('add', 5, 3), 8)
        self.assertEqual(get_operation_result('subtract', 10, 4), 6)
        self.assertEqual(get_operation_result('multiply', 6, 7), 42)
        self.assertEqual(get_operation_result('divide', 15, 3), 5)
    
    def test_invalid_operation(self):
        """Test invalid operation raises ValueError."""
        with self.assertRaises(ValueError):
            get_operation_result('power', 2, 3)
        
        with self.assertRaises(ValueError):
            get_operation_result('modulo', 10, 3)
    
    def test_divide_by_zero_through_dispatcher(self):
        """Test division by zero through dispatcher."""
        with self.assertRaises(ValueError):
            get_operation_result('divide', 10, 0)


# Pytest-style tests for GitHub Actions compatibility
def test_add_positive_numbers():
    """Test adding positive numbers."""
    assert add(2, 3) == 5

def test_add_negative_numbers():
    """Test adding negative numbers."""
    assert add(-2, -3) == -5

def test_subtract_basic():
    """Test basic subtraction."""
    assert subtract(10, 3) == 7

def test_multiply_basic():
    """Test basic multiplication."""
    assert multiply(4, 5) == 20

def test_divide_basic():
    """Test basic division."""
    assert divide(12, 3) == 4

def test_divide_zero_error():
    """Test that dividing by zero raises an error."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_operation_dispatcher():
    """Test the operation dispatcher function."""
    assert get_operation_result('add', 1, 2) == 3
    assert get_operation_result('multiply', 3, 4) == 12

def test_invalid_operation_error():
    """Test that invalid operations raise errors."""
    with pytest.raises(ValueError, match="Unknown operation"):
        get_operation_result('invalid', 1, 2)


if __name__ == '__main__':
    # Run tests when script is executed directly
    unittest.main(verbosity=2)
