# TESTS/test_levels_handler.py
import unittest
import sys
import os
import asyncio
import pygame  # type: ignore
# Set work directory to the root directory of the project
os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Add the root directory to the Python path
sys.path.append(os.getcwd())
from UI.intro import name_input_validate

class TestNameValidation(unittest.TestCase):
    def test_valid_name(self):
        self.assertTrue(name_input_validate("TestName"))  # Valid name
    
    def test_empty_name(self):
        self.assertFalse(name_input_validate(""))  # Empty name
    
    def test_long_name(self):
        self.assertFalse(name_input_validate("A" * 11))  # Name exceeds 10 characters
    
    def test_invalid_characters(self):
        self.assertFalse(name_input_validate("Test_Name"))
        self.assertFalse(name_input_validate("Test/Name"))
        self.assertFalse(name_input_validate("Test-Name"))
    
    def test_only_spaces(self):
        self.assertFalse(name_input_validate("   "))  # Only spaces

if __name__ == "__main__":
    unittest.main()