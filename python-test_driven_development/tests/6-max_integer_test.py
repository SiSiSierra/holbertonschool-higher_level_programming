#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
import sys
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):


    def test_positive(self):
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([5, 55, 100000, 2]), 100000)
        self.assertEqual(max_integer([99, 1, 2]), 99)
        self.assertEqual(max_integer([5]), 5)

    def test_negative(self):
        self.assertEqual(max_integer([-5, 5]), 5)
        self.assertEqual(max_integer([-99, -4, -20]), -4)

    def test_null(self):
        self.assertEqual(None, max_integer([]))
        self.assertEqual(None, max_integer())
    
    def test_type_error(self):
        self.assertRaises(TypeError, max_integer('1'))
        self.assertRaises(TypeError, max_integer(['1']))
        self.assertRaises(TypeError, max_integer([[1], [2]]))

    def test_float(self):
        self.assertEqual(2.5, max_integer([1, -4, 2.5]))
        self.assertEqual(-1, max_integer([-43.6, -1, -1.1]))
