#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """This is the test class"""
    def test_NormalList(self):
        list = [5, 9, 3, 6]
        self.assertEqual(max_integer(list), 9)

    def test_Floats(self):
        list = [4.2, 14.5, 3.1, 15.8, 9.0, 2.7]
        self.assertEqual(max_integer(list), 15.8)

    def test_Empty(self):
        list = []
        self.assertEqual(max_integer(list), None)
