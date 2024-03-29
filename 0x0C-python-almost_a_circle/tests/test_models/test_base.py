#!/usr/bin/python3

import unittest
from .. import base


def test_normal(self):
    b1 = Base()
    self.assertEqual(b1.id, 1)

def test_abnormal(self):
    b2 = Base(12)
    self.assertEqual(b2.id, 12)
